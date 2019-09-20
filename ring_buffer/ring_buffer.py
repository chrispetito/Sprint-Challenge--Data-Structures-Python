class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # replace current index with item
    self.storage[self.current] = item
    # increment self.current
    self.current += 1
    print(self.storage)
    # if self.current is at capacity...
    if self.current == self.capacity:
        # return current to index of 0 and start again
        self.current = 0

  def get(self):
    new_list = []
    for val in self.storage:
      if val != None:
        new_list.append(val)

    return new_list