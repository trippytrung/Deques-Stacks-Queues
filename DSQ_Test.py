import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    self.__deque = get_deque()
    self.__stack = Stack()
    self.__queue = Queue()

  # TODO add your test methods here. Like Linked_List_Test.py,
  # each test should me in a method whose name begins with test_

  
#deque tests

  def test_empty_list_string(self):
    self.assertEqual('[ ]', str(self.__deque), 'Empty list should print as "[ ]"')
    self.assertEqual(0, len(self.__deque))

  def test_push_front_empty(self):
    self.__deque.push_front('Victory')
    self.assertEqual('[ Victory ]', str(self.__deque))
    self.assertEqual(1, len(self.__deque))

  def test_push_back_empty(self):
    self.__deque.push_back('Victory')
    self.assertEqual('[ Victory ]', str(self.__deque))
    self.assertEqual(1, len(self.__deque))

  def test_push_front_with_one(self):
    self.__deque.push_front('Structures')
    self.__deque.push_front('Data')
    self.assertEqual('[ Data, Structures ]', str(self.__deque))
    self.assertEqual(2, len(self.__deque))

  def test_push_front_with_one(self):
    self.__deque.push_back('Structures')
    self.__deque.push_front('Data')
    self.assertEqual('[ Data, Structures ]', str(self.__deque))
    self.assertEqual(2, len(self.__deque))

  def test_push_back_with_one(self):
    self.__deque.push_back('Data')
    self.__deque.push_back('Structures')
    self.assertEqual('[ Data, Structures ]', str(self.__deque))
    self.assertEqual(2, len(self.__deque))

  def test_push_back_with_one(self):
    self.__deque.push_front('Data')
    self.__deque.push_back('Structures')
    self.assertEqual('[ Data, Structures ]', str(self.__deque))
    self.assertEqual(2, len(self.__deque))
#------------------
  def test_push_front_with_two(self):
    self.__deque.push_front('Structures')
    self.__deque.push_front('Data')
    self.__deque.push_front('Victory')
    self.assertEqual('[ Victory, Data, Structures ]', str(self.__deque))
    self.assertEqual(3, len(self.__deque))

  def test_push_back_with_two(self):
    self.__deque.push_front('Structures')
    self.__deque.push_front('Data')
    self.__deque.push_back('Victory')
    self.assertEqual('[ Data, Structures, Victory ]', str(self.__deque))
    self.assertEqual(3, len(self.__deque))

  def test_push_front_with_two(self):
    self.__deque.push_back('Structures')
    self.__deque.push_front('Data')
    self.__deque.push_front('Victory')
    self.assertEqual('[ Victory, Data, Structures ]', str(self.__deque))
    self.assertEqual(3, len(self.__deque))

  def test_push_back_with_two(self):
    self.__deque.push_back('Structures')
    self.__deque.push_front('Data')
    self.__deque.push_back('Victory')
    self.assertEqual('[ Data, Structures, Victory ]', str(self.__deque))
    self.assertEqual(3, len(self.__deque))

  def test_push_front_with_two(self):
    self.__deque.push_back('Data')
    self.__deque.push_back('Structures')
    self.__deque.push_front('Victory')
    self.assertEqual('[ Victory, Data, Structures ]', str(self.__deque))
    self.assertEqual(3, len(self.__deque))

  def test_push_back_with_two(self):
    self.__deque.push_back('Data')
    self.__deque.push_back('Structures')
    self.__deque.push_back('Victory')
    self.assertEqual('[ Data, Structures, Victory ]', str(self.__deque))
    self.assertEqual(3, len(self.__deque))

  def test_push_front_with_two(self):
    self.__deque.push_front('Data')
    self.__deque.push_back('Structures')
    self.__deque.push_front('Victory')
    self.assertEqual('[ Victory, Data, Structures ]', str(self.__deque))
    self.assertEqual(3, len(self.__deque))

  def test_push_back_with_two(self):
    self.__deque.push_front('Data')
    self.__deque.push_back('Structures')
    self.__deque.push_back('Victory')
    self.assertEqual('[ Data, Structures, Victory ]', str(self.__deque))
    self.assertEqual(3, len(self.__deque))
#-----------
  def test_pop_front_empty(self):
    val = self.__deque.pop_front()
    self.assertEqual(None, val)
    self.assertEqual(0, len(self.__deque))

  def test_pop_back_empty(self):
    val = self.__deque.pop_front()
    self.assertEqual(None, val)
    self.assertEqual(0, len(self.__deque))

  def test_pop_front_with_one(self):
    self.__deque.push_front('Structures')
    val=self.__deque.pop_front()
    self.assertEqual('Structures', val)
    self.assertEqual(0, len(self.__deque))

  def test_pop_back_with_one(self):
    self.__deque.push_front('Structures')
    val=self.__deque.pop_back()
    self.assertEqual('Structures', val)
    self.assertEqual(0, len(self.__deque))

  def test_pop_front_with_two(self):
    self.__deque.push_back('Data')
    self.__deque.push_back('Structures')
    val = self.__deque.pop_front()
    self.assertEqual('Data',val)
    self.assertEqual(1, len(self.__deque))

  def test_pop_back_with_two(self):
    self.__deque.push_back('Data')
    self.__deque.push_back('Structures')
    val = self.__deque.pop_back()
    self.assertEqual('Structures',val)
    self.assertEqual(1, len(self.__deque))
#------------------
  def test_peek_front_empty(self):
    val = self.__deque.peek_front()
    self.assertEqual(None, val)
    self.assertEqual(0, len(self.__deque))

  def test_peek_back_empty(self):
    val = self.__deque.peek_front()
    self.assertEqual(None, val)
    self.assertEqual(0, len(self.__deque))

  def test_peek_front_with_one(self):
    self.__deque.push_front('Structures')
    val=self.__deque.peek_front()
    self.assertEqual('Structures', val)
    self.assertEqual(1, len(self.__deque))

  def test_peek_back_with_one(self):
    self.__deque.push_front('Structures')
    val=self.__deque.peek_back()
    self.assertEqual('Structures', val)
    self.assertEqual(1, len(self.__deque))

  def test_peek_front_with_two(self):
    self.__deque.push_back('Data')
    self.__deque.push_back('Structures')
    val = self.__deque.peek_front()
    self.assertEqual('Data',val)
    self.assertEqual(2, len(self.__deque))

  def test_peek_back_with_two(self):
    self.__deque.push_back('Data')
    self.__deque.push_back('Structures')
    val = self.__deque.peek_back()
    self.assertEqual('Structures',val)
    self.assertEqual(2, len(self.__deque))

#stack tests

  def test_empty_list_string(self):
    self.assertEqual('[ ]', str(self.__stack), 'Empty list should print as "[ ]"')
    self.assertEqual(0, len(self.__stack))

  def test_push_empty(self):
    self.__stack.push('Victory')
    self.assertEqual('[ Victory ]', str(self.__stack))
    self.assertEqual(1, len(self.__stack))

  def test_push_with_one(self):
    self.__stack.push('Structures')
    self.__stack.push('Data')
    self.assertEqual('[ Data, Structures ]', str(self.__stack))
    self.assertEqual(2, len(self.__stack))

  def test_push_with_two(self):
    self.__stack.push('Structures')
    self.__stack.push('Data')
    self.__stack.push('Victory')
    self.assertEqual('[ Victory, Data, Structures ]', str(self.__stack))
    self.assertEqual(3, len(self.__stack))
#-----------
  def test_pop_empty(self):
    val = self.__stack.pop()
    self.assertEqual(None, val)
    self.assertEqual(0, len(self.__stack))

  def test_pop_with_one(self):
    self.__stack.push('Structures')
    val=self.__stack.pop()
    self.assertEqual('Structures', val)
    self.assertEqual(0, len(self.__stack))

  def test_pop_with_two(self):
    self.__stack.push('Data')
    self.__stack.push('Structures')
    val = self.__stack.pop()
    self.assertEqual('Structures',val)
    self.assertEqual(1, len(self.__stack))
#------------------
  def test_peek_empty(self):
    val = self.__stack.peek()
    self.assertEqual(None, val)
    self.assertEqual(0, len(self.__stack))


  def test_peek_with_one(self):
    self.__stack.push('Structures')
    val=self.__stack.peek()
    self.assertEqual('Structures', val)
    self.assertEqual(1, len(self.__stack))

  def test_peek_with_two(self):
    self.__stack.push('Data')
    self.__stack.push('Structures')
    val = self.__stack.peek()
    self.assertEqual('Data',val)
    self.assertEqual(2, len(self.__stack))

#queue tests

  def test_empty_list_string(self):
    self.assertEqual('[ ]', str(self.__queue), 'Empty list should print as "[ ]"')
    self.assertEqual(0, len(self.__queue))

  def test_enqueue_empty(self):
    self.__queue.enqueue('Victory')
    self.assertEqual('[ Victory ]', str(self.__queue))
    self.assertEqual(1, len(self.__queue))

  def test_enqueue_with_one(self):
    self.__queue.enqueue('Data')
    self.__queue.enqueue('Structures')
    self.assertEqual('[ Data, Structures ]', str(self.__queue))
    self.assertEqual(2, len(self.__queue))

  def test_enqueue_with_two(self):
    self.__queue.enqueue('Victory')
    self.__queue.enqueue('Data')
    self.__queue.enqueue('Structures')
    self.assertEqual('[ Victory, Data, Structures ]', str(self.__queue))
    self.assertEqual(3, len(self.__queue))
#-----------
  def test_dequeue_empty(self):
    val = self.__queue.dequeue()
    self.assertEqual(None, val)
    self.assertEqual(0, len(self.__queue))

  def test_dequeue_with_one(self):
    self.__queue.enqueue('Structures')
    val=self.__queue.dequeue()
    self.assertEqual('Structures', val)
    self.assertEqual(0, len(self.__queue))

  def test_dequeue_with_two(self):
    self.__queue.enqueue('Data')
    self.__queue.enqueue('Structures')
    val = self.__queue.dequeue()
    self.assertEqual('Data',val)
    self.assertEqual(1, len(self.__queue))
#------------------
  def test_peek_empty(self):
    val = self.__queue.peek()
    self.assertEqual(None, val)
    self.assertEqual(0, len(self.__queue))

  def test_peek_with_one(self):
    self.__queue.enqueue('Structures')
    val=self.__queue.peek()
    self.assertEqual('Structures', val)
    self.assertEqual(1, len(self.__queue))

  def test_peek_with_two(self):
    self.__queue.enqueue('Data')
    self.__queue.enqueue('Structures')
    val = self.__queue.peek()
    self.assertEqual('Data',val)
    self.assertEqual(2, len(self.__queue))


if __name__ == '__main__':
  unittest.main()
