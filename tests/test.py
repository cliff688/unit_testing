import unittest
from algorithms.algorithms.binarysearch import binary_search

class BinarySearchTest(unittest.TestCase):


    def test_all_elements_in_an_odd_length_list(self):
        """All elements in a given list should return true to test"""
        odd_length_array = list(range(5))
        even_length_array = list(range(6))

        for element in odd_length_array:
            with self.subTest(msg="Testing in array with odd length.", element=element):
                self.assertTrue(binary_search(odd_length_array, element))
        for element in even_length_array:
            with self.subTest(msg="Testing in array with even length.", element=element):
                self.assertTrue(binary_search(even_length_array, element))

    def test_for_element_not_in_array(self):
        """elements not in the array should return false"""
        array = list(range(2))
        element_not_in_array = 3
        self.assertFalse(binary_search(array, element_not_in_array))

    def test_empty_array(self):
        """This should not raise an error"""
        self.assertFalse(binary_search([],0))


if __name__ == "__main__":
    unittest.main()