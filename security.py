from config import BLOCKED_IPS, BLOCKED_KEYWORDS

def is_blocked_ip(ip):
    return ip in BLOCKED_IPS

def is_blocked_keyword(response):
    for word in BLOCKED_KEYWORDS:
        if word.encode() in response:
            return True
    return False

def is_blocked(url):
    return "example.com" in url
