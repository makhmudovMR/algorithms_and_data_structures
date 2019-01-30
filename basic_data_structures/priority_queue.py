class PQueue:

    def __init__(self):
        self.queue = []
        self.priority = []

    def add(self, data, p=0):
        self.queue.insert(0,data)
        self.priority.insert(0,data)
