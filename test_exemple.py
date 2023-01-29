import unittest
from script import Robot
from script import replace_all_0_by_1, set_tableau

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
    
    def test_array_3(self):
        test_array = [[0 for i in range(66)] for j in range(66)]
        for i in range(66):
            test_array[i][0] = -1
            test_array[i][65] = -1
            test_array[0][i] = -1
            test_array[65][i] = -1
        
        robot = Robot(66, test_array)
        expected_tab = replace_all_0_by_1(test_array)
        result = robot.scan()

        self.assertEqual(result, expected_tab)
    
    def test_array_4(self):
        test_array =[[-1, -1, -1, -1, -1],
                    [-1, 0, 0, 0, -1],
                    [-1, 0, -1, 0, -1],
                    [-1, 0, 0, 0, -1],
                    [-1, -1, -1, -1, -1]]
        robot = Robot(5, test_array)
        expected_tab = replace_all_0_by_1(test_array)
        result = robot.scan()

        self.assertEqual(result, expected_tab)
    
    def test_array_4(self):
        test_array = set_tableau(66)
        robot = Robot(66, test_array)
        expected_tab = replace_all_0_by_1(test_array)
        result = robot.scan()

        self.assertEqual(result, expected_tab)
    
        

if __name__ == '__main__':
    unittest.main()
