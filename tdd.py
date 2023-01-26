import unittest
from script import Robot


class TestArray(unittest.TestCase):
    
    def setUp(self) -> None:
        return super().setUp()
    
    def test_1(self):
        robot = Robot(3)
        a = robot.scan()
        b = a        

if __name__ == '__main__':
    unittest.main()
    

