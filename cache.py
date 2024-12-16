import time
from config import CACHE_TIME

class Cache:
    def __init__(self):
        self.store = {}

    def get(self, key):
        if key in self.store and (time.time() - self.store[key]['time']) < CACHE_TIME:
            return self.store[key]['data']
        return None

    def set(self, key, data):
        self.store[key] = {'data': data, 'time': time.time()}
