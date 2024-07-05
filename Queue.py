from Deque_Generator import get_deque

class Queue:

  def __init__(self):
    self.__dq = get_deque()

  def __str__(self):
    # TODO replace pass with your implementation.
    # Orient your string from front (left) to back (right).
    return str(self.__dq)

  def __len__(self):
    # TODO replace pass with your implementation.
    return len(self.__dq)

  def enqueue(self, val):
    # TODO replace pass with your implementation.
    self.__dq.push_back(val)

  def dequeue(self):
    # TODO replace pass with your implementation.
    value=self.__dq.pop_front()
    return value

  def peek(self):
    # TODO replace pass with your implementation.
    value=self.__dq.peek_front()
    return value

# Unit tests make the main section unneccessary.
# if __name__ == '__main__':
#   pass
