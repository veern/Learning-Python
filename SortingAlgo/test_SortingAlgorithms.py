import unittest
from SortingAlgorithms import bubble_sort, insert_sort, selection_sort
from random import randint, uniform

class Test_sorting_algorithms(unittest.TestCase):

    def test_bubble_sort(self) -> None:
        self.assertEqual(bubble_sort([1,2,3,4,5]), [1,2,3,4,5])
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([12,3,1,5,1,2,3,124,3,2,1]), [1,1,1,2,2,3,3,3,5,12,124])
        
        testlst = [randint(1, 100) for x in range(1, 1000)]
        self.assertEqual(bubble_sort(testlst), sorted(testlst))

        testlst2 = [randint(-10000, 10000) for x in range(1, 1000)]
        self.assertEqual(bubble_sort(testlst2), sorted(testlst2))

        testfloat = [uniform(-1000, 1000) for x in range(1, 1000)]
        self.assertEqual(bubble_sort(testfloat), sorted(testfloat))

        with self.assertRaises(TypeError):
            bubble_sort([1+0.2j, 3+0.4j, 4+0.1j])

        with self.assertRaises(TypeError):
            bubble_sort([1,"a",[]])
        
        with self.assertRaises(TypeError):
            bubble_sort(["", "", "randomstring"])

        with self.assertRaises(TypeError):
            bubble_sort("")

    def test_insert_sort(self):
        self.assertEqual(insert_sort([1,2,3,4,5]), [1,2,3,4,5])
        self.assertEqual(insert_sort([]), [])
        self.assertEqual(insert_sort([12,3,1,5,1,2,3,124,3,2,1]), [1,1,1,2,2,3,3,3,5,12,124])
        
        testlst = [randint(1, 100) for x in range(1, 1000)]
        self.assertEqual(insert_sort(testlst), sorted(testlst))

        testlst2 = [randint(-10000, 10000) for x in range(1, 1000)]
        self.assertEqual(insert_sort(testlst2), sorted(testlst2))

        testfloat = [uniform(-1000, 1000) for x in range(1, 1000)]
        self.assertEqual(insert_sort(testfloat), sorted(testfloat))

        with self.assertRaises(TypeError):
            insert_sort([1+0.2j, 3+0.4j, 4+0.1j])

        with self.assertRaises(TypeError):
            insert_sort([1,"a",[]])
        
        with self.assertRaises(TypeError):
            insert_sort(["", "", "randomstring"])

        with self.assertRaises(TypeError):
            insert_sort("")

    def test_selection_sort(self):
        self.assertEqual(selection_sort([1,2,3,4,5]), [1,2,3,4,5])
        self.assertEqual(selection_sort([]), [])
        self.assertEqual(selection_sort([12,3,1,5,1,2,3,124,3,2,1]), [1,1,1,2,2,3,3,3,5,12,124])
        
        testlst = [randint(1, 100) for x in range(1, 1000)]
        self.assertEqual(selection_sort(testlst), sorted(testlst))

        testlst2 = [randint(-10000, 10000) for x in range(1, 1000)]
        self.assertEqual(selection_sort(testlst2), sorted(testlst2))

        testfloat = [uniform(-1000, 1000) for x in range(1, 1000)]
        self.assertEqual(selection_sort(testfloat), sorted(testfloat))

        with self.assertRaises(TypeError):
            selection_sort([1+0.2j, 3+0.4j, 4+0.1j])

        with self.assertRaises(TypeError):
            selection_sort([1,"a",[]])
        
        with self.assertRaises(TypeError):
            selection_sort(["", "", "randomstring"])

        with self.assertRaises(TypeError):
            selection_sort("")