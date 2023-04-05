import unittest
import machinetranslation

class TestTranslate(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(machinetranslation.translator.english_to_french('Hello'),'Bonjour')
        self.assertEqual(machinetranslation.translator.english_to_french(''),'')

    def test_french_to_english(self):        
        self.assertEqual(machinetranslation.translator.french_to_english('Bonjour'),'Hello')
        self.assertEqual(machinetranslation.translator.french_to_english(''),'')

unittest.main()