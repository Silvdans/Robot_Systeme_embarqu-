import unittest
from script import Robot
from script import replace_all_0_by_1

class Test_Array(unittest.TestCase):

    def test_array_1(self):
        test_array =[[-1, -1, -1],
            [-1, -0, -1],
            [-1, -1, -1]]
        robot = Robot(3, test_array)
        
        result = robot.scan()
        expected_tab = replace_all_0_by_1(test_array)
        self.assertEqual(result, expected_tab)
    
    def test_array_2(self):
        test_array =[[-1, -1, -1, -1, -1],
                    [-1, 0, 0, 0, -1],
                    [-1, 0, 0, 0, -1],
                    [-1, 0, 0, 0, -1],
                    [-1, -1, -1, -1, -1]]
        robot = Robot(5, test_array)
        expected_tab = replace_all_0_by_1(test_array)
        result = robot.scan()
        
        self.assertEqual(result, expected_tab)


if __name__ == '__main__':
    unittest.main()
