class Queue:

    def __init__(self):
        self.queue = []

    def addq(self, v):
        # add an element to the queue
        self.queue.append(v)

    def delq(self):
        # remove an element from the queue
        v = None

        if not self.isempty():
            v = self.queue[0]
            self.queue = self.queue[1:]

        return v

    def isempty(self):
        return self.queue == []

    def __str__(self):
        return str(self.queue)


# For demo purposes only
q = Queue()

for i in range(3):
    q.addq(i)
    print(q)

print(q.isempty())

for i in range(3):
    print(q.delq(), q)

print(q.isempty())