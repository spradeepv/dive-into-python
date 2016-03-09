"""

"""
from collections import deque


class Palindrome:
    def __init__(self):
        self.stack = []
        self.queue = deque()

    def pushCharacter(self, ch):
        """Pushes a character onto a stack."""
        self.stack.append(ch)

    def enqueueCharacter(self, ch):
        """Enqueues a character in a queue."""
        self.queue.append(ch)

    def popCharacter(self):
        """Pops and returns the top character."""
        return self.stack.pop()

    def dequeueCharacter(self):
        """Dequeues and returns the first character."""
        return self.queue.popleft()
