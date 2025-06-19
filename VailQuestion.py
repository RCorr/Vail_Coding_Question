import time
import unittest

"""
Question:

The problem we would like you to solve deals with an array of integers. We want to rotate these integers
to a specified number of positions to the left.

If for example you have an array of integers [1,2,3,4,5,6,7] and we would like to rotate 2 positions to the
left, the solution expected would be [3,4,5,6,7,1,2].

Note: the solution should be able to handle a position value greater than the number of integers in the
array. If, for example, we would like to rotate [1,2,3,4,5,6,7] 8 positions to left, it would produce the
result [2,3,4,5,6,7,1]. Negative values for the positions to rotate will throw an error which the code
example should handle gracefully.


assumptions:
- any input other than a list of integers for the array will throw an error. Alternatively, tuples and ranges could be converted into lists
- any input other than an integer for the rotation will throw an error. Alternatively, floats could be converted into ints
"""


"""
Args:
    param1: An integer array to be rotated
    param2: An integer value of the number of positions to be rotated

Returns:
    Returns a new array

Raises:
    TypeError: If param1 is not a list of integers
    TypeError: If param2 is not an integer
    ValueError: If param2 is negative
"""
def rotate_array(array : list[int], rotation : int) -> list[int]:
    if not isinstance(array, list):
        raise TypeError("Please use an integer list array")
    
    if len(array) == 0: # Degenerate case
        return []

    if not isinstance(array[0], int):
        raise TypeError("Please use an integer list array")

    if not isinstance(rotation, int):
        raise TypeError("Please use an integer rotation value")

    if rotation < 0:
        raise ValueError("Please use a non-negative rotation value")
    
    mod_rotation = rotation % len(array) # Optimization significantly reduces runtime if the rotation is larger than the array
    return array[mod_rotation:] + array[:mod_rotation] # A simple and fast method, runs in O(1) time



class TestMethods(unittest.TestCase):
    # Testing short rotation cases
    def test_rotate_3_by_1(self):
        self.assertEqual(rotate_array([1, 2, 3], 1), [2, 3, 1])

    def test_rotate_3_by_2(self):
        self.assertEqual(rotate_array([1, 2, 3], 2), [3, 1, 2])

    def test_rotate_7_by_2(self):
        self.assertEqual(rotate_array([1, 2, 3, 4, 5, 6, 7], 2), [3, 4, 5, 6, 7, 1, 2])

    def test_rotate_7_by_5(self):
        self.assertEqual(rotate_array([1, 2, 3, 4, 5, 6, 7], 5), [6, 7, 1, 2, 3, 4, 5])

    def test_rotate_7_by_9(self):
        self.assertEqual(rotate_array([1, 2, 3, 4, 5, 6, 7], 9), [3, 4, 5, 6, 7, 1, 2])
    
    def test_rotate_empty_by_1(self):
        self.assertEqual(rotate_array([], 1), [])

    # Testing long rotation cases, with time limit
    def test_rotate_7_by_99999(self):
        start_time = time.time()
        self.assertEqual(rotate_array([1, 2, 3, 4, 5, 6, 7], 99999), [5, 6, 7, 1, 2, 3, 4])
        self.assertLess((time.time() - start_time), 0.1)

    def test_rotate_99998_by_1(self):
        start_time = time.time()
        self.assertEqual(rotate_array(list(range(1, 99999)), 1), (list(range(2, 99999))+[1]))
        self.assertLess((time.time() - start_time), 0.1)

    def test_rotate_99998_by_99997(self):
        start_time = time.time()
        self.assertEqual(rotate_array(list(range(1, 99999)), 99997), ([99998]+list(range(1, 99998))))
        self.assertLess((time.time() - start_time), 0.1)

    def test_rotate_99998_by_99999(self):
        start_time = time.time()
        self.assertEqual(rotate_array(list(range(1, 99999)), 99999), (list(range(2, 99999))+[1]))
        self.assertLess((time.time() - start_time), 0.1)


    # Testing strange and wrong inputs, should throw errors
    def test_string_instead_of_array_error(self):
        try:
            rotate_array("s", 1)
            assert False, "Expected TypeError"
        except TypeError:
            pass
    
    def test_string_array_instead_of_array_error(self):
        try:
            rotate_array(["s"], 1)
            assert False, "Expected TypeError"
        except TypeError:
            pass
    
    def test_tuple_instead_of_array_error(self):
        try:
            rotate_array((1, 2, 3), 1)
            assert False, "Expected TypeError"
        except TypeError:
            pass

    def test_range_instead_of_array_error(self):
        try:
            rotate_array(range(4), 1)
            assert False, "Expected TypeError"
        except TypeError:
            pass
    
    def test_None_instead_of_array_error(self):
        try:
            rotate_array(None, 1)
            assert False, "Expected TypeError"
        except TypeError:
            pass

    def test_string_instead_of_int_error(self):
        try:
            rotate_array([1, 2, 3], "s")
            assert False, "Expected TypeError"
        except TypeError:
            pass
    
    def test_string_instead_of_int_error(self):
        try:
            rotate_array([1, 2, 3], 1.5)
            assert False, "Expected TypeError"
        except TypeError:
            pass

    def test_string_instead_of_int_error(self):
        try:
            rotate_array([1, 2, 3], (3 + 2j))
            assert False, "Expected TypeError"
        except TypeError:
            pass

    def test_string_instead_of_int_error(self):
        try:
            rotate_array([1, 2, 3], None)
            assert False, "Expected TypeError"
        except TypeError:
            pass

    def test_string_instead_of_int_error(self):
        try:
            rotate_array([1, 2, 3], -1)
            assert False, "Expected ValueError"
        except ValueError:
            pass


if __name__ == '__main__':
    test = list(range(1, 8))
    print(rotate_array(test, 2))
    unittest.main()