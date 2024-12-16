class Stats:
    def __init__(self):
        self.request_count = {}

    def increment(self, domain):
        self.request_count[domain] = self.request_count.get(domain, 0) + 1

    def display(self):
        for domain, count in self.request_count.items():
            print(f"{domain}: {count} requests")
