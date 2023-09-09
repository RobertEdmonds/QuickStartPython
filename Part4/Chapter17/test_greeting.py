"""Test the greeting file"""
# pylint: disable=no-member
# import unittest
    # It is a module used for testing
import unittest

# Import the file you would like to test
import greeting

# Write a class for the testing
class GreetingTest(unittest.TestCase):
    def test_greeting_without_name(self):
        # Test without a name
        self.assertEqual(greeting.greetings(), "Well Hello, World!")

    names = [
            "Tom",
            "Robert",
            "Marry"
        ]
    
    def test_greeting_with_name(self):
        for name in self.names:
            # test with input
            print(greeting.greetings(name))
            self.assertEqual(greeting.greetings(name), f"Well Hello, {name}!")

    def test_writing_file(self):
        self.assertTrue(greeting.write_file(data=4, filename="test.txt"))

if __name__ == '__main__':
    unittest.main()
