"""Testcase for Translator"""
import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslation(unittest.TestCase):
    """Translation test cases"""
    def testEnglishToFrench(self):
        """
        English to French test
        For some reason, mymemory api translates "Hello" to "Pepitoooo".
        It translates correctly in lowercase.
        """
        self.assertEqual(englishToFrench("hello"), "bonjour")

    def testFrenchToEnglish(self):
        """
        French to English test
        """
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

unittest.main()
