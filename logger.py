import logging

logging.basicConfig(filename='proxy.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_request(url, status):
    logging.info(f"request: {url} | status: {status}")

def log_error(message):
    logging.error(f"error: {message}")
