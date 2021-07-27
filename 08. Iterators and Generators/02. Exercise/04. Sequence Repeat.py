from collections import deque

class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.number:
            raise StopIteration
        self.current += 1
        self.sequence = deque(self.sequence)
        character = self.sequence.popleft()
        self.sequence.append(character)
        return character


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
