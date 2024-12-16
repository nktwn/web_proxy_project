import socket
import threading
from cache import Cache
from logger import log_request, log_error
from security import is_blocked_ip, is_blocked_keyword, is_blocked
from stats import Stats
from config import HOST, PORT, BUFFER_SIZE, MAX_CONNECTIONS

cache = Cache()
stats = Stats()
active_connections = threading.Semaphore(MAX_CONNECTIONS)

def handle_client(client_socket, client_address):
    try:
        request = client_socket.recv(BUFFER_SIZE).decode('utf-8', errors='ignore')
        if not request:
            return

        first_line = request.split('\n')[0]
        method, url, _ = first_line.split()

        if "ocsp" in url or "lencr.org" in url:
            client_socket.send(b"HTTP/1.1 204 No Content\r\n\r\n")
            log_request(url, "204 No Content")
            return

        if method == "CONNECT":
            handle_https(client_socket, url)
            return

        client_socket.send(b"HTTP/1.1 405 Method Not Allowed\r\n\r\n")
        log_request(url, "405 Method Not Allowed")

    except Exception as e:
        log_error(f"error: {e}")
    finally:
        client_socket.close()

def handle_https(client_socket, url):
    try:
        target_host, target_port = url.split(":")
        target_port = int(target_port)
        print(f"[log] https connect to {target_host}:{target_port}")
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.connect((target_host, target_port))
        client_socket.send(b"HTTP/1.1 200 Connection Established\r\n\r\n")
        forward_data(client_socket, server_socket)
        log_request(f"{target_host}:{target_port}", "200 OK (HTTPS CONNECT)")
    except Exception as e:
        log_error(f"error handling connect to {url}: {e}")

def forward_data(client_socket, server_socket):
    sockets = [client_socket, server_socket]
    while True:
        for sock in sockets:
            data = sock.recv(BUFFER_SIZE)
            if not data:
                return
            other_sock = server_socket if sock == client_socket else client_socket
            other_sock.sendall(data)

def start_server():
    print(f"proxy server running on {HOST}:{PORT}")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    while True:
        client_socket, client_address = server.accept()
        threading.Thread(target=handle_client, args=(client_socket, client_address)).start()

if __name__ == "__main__":
    start_server()
