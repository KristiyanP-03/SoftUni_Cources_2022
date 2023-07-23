class Cat:

  def __init__(self, name):
    self.name = name
    self.fed = False
    self.sleepy = False
    self.size = 0

  def eat(self):
    if self.fed:
      raise Exception('Already fed.')

    self.fed = True
    self.sleepy = True
    self.size += 1

  def sleep(self):
    if not self.fed:
      raise Exception('Cannot sleep while hungry')

    self.sleepy = False

import unittest
class CatTests(unittest.TestCase):

  def setUp(self) -> None:
    self.cat = Cat("Cat")

  def test_cat_size_increasing_after_eating(self):
    self.cat.eat()
    self.assertEqual(self.cat.size, 1)

  def test_cat_is_fed_after_eating(self):
    self.cat.eat()
    self.assertTrue(self.cat.fed)

  def test_cat_is_already_fed(self):
    self.cat.eat()
    with self.assertRaises(Exception) as routine:
      self.cat.eat()
    self.assertEqual(str(routine.exception), 'Already fed.')

  def test_cat_can_not_sleep_hungry(self):
    with self.assertRaises(Exception) as warning:
      self.cat.sleep()
    self.assertEqual(str(warning.exception), 'Cannot sleep while hungry')

  def test_cat_is_not_sleepy_after_sleep(self):
    self.cat.eat()
    self.cat.sleep()
    self.assertFalse(self.cat.sleepy)

if __name__ == '__main__':
  unittest.main()