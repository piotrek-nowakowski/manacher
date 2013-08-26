import unittest
import time

import manacher

class TestGetPalindromeLength(unittest.TestCase):

    def test_no_palindrome(self):
        string = 'abc'
        self.assertEqual(manacher.get_palindrome_length(string, 1), 0)
    
    def test_left_border(self):
        string = 'abc'
        self.assertEqual(manacher.get_palindrome_length(string, 0), 0)

    def test_right_border(self):
        string = 'abc'
        self.assertEqual(manacher.get_palindrome_length(string, 2), 0)
    
    def test_palindrome(self):
        string = 'abbbc'
        self.assertEqual(manacher.get_palindrome_length(string, 2), 1)

class TestManacher(unittest.TestCase):
    
    def test_same_char(self):
        input_data = 'a'*5
        expected = [0, 0, 1, 1, 2, 2, 2, 1, 1, 0, 0]
        self.assertEqual(manacher.manacher(input_data), expected)
      
    def test_no_overlap(self):
        input_data = 'aapmm'
        expected = [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
        self.assertEqual(manacher.manacher(input_data), expected)
        
    def test_no_palindromes(self):
        input_data = 'abcdefghijklmonp'
        expected = [0 for e in xrange(len(input_data) * 2 + 1)] 
        self.assertEqual(manacher.manacher(input_data), expected)
        
    def test_time_complexity(self):
        
        def timed_run(string):
            start = time.time()
            manacher.manacher(string)
            return time.time() - start
        
        results = map(lambda e: timed_run('a'*e), xrange(100, 1000, 100))
        for small, big in zip(results[1:], results[:-1]):
            self.assertGreater(small*10, big)


class TestGetPalindromeNumber(unittest.TestCase):
    
    def test_no_palindromes(self):
        input_data = 'abcdefghijklmnoprst'
        expected = 0
        self.assertEqual(manacher.get_palindrome_number(input_data), expected)
        
    def test_palindromes(self):
        input_data = 'q'*5
        expected = 10
        print manacher.manacher(input_data)
        self.assertEqual(manacher.get_palindrome_number(input_data), expected)