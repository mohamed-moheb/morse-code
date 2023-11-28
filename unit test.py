import unittest
from morse_code import encryption, decryption


class EncryptionTests(unittest.TestCase):

    # Test empty string
    def test_encryption_empty_string(self):
        """
        Test that encryption() returns an empty string when given an empty input string.
        """
        input_phrase = ""
        expected_output = ""

        actual_output = encryption(input_phrase)

        self.assertEqual(actual_output, expected_output)

    # Test single word
    def test_encryption_single_word(self):
        """
        Test that encryption() correctly converts a single word to its corresponding Morse code representation.
        """
        input_phrase = "hello"
        expected_output = "... . .-.. .-.. ---"

        actual_output = encryption(input_phrase)

        self.assertEqual(actual_output, expected_output)

    # Test multiple words
    def test_encryption_multiple_words(self):
        """
        Test that encryption() correctly converts a phrase of multiple words to their corresponding Morse code representation, including spaces.
        """
        input_phrase = "this is a test"
        expected_output = "- .... .. ... / .--. .-. . -.- ... - / .-. .. ...- .-. .-.. ---"

        actual_output = encryption(input_phrase)

        self.assertEqual(actual_output, expected_output)

    # Test mixed-case phrase
    def test_encryption_mixed_case_phrase(self):
        """
        Test that encryption() correctly handles phrases with mixed-case letters, preserving the original case in the Morse code output.
        """
        input_phrase = "UPPER lower"
        expected_output = "..- .--. .--. . .-. / .-.. --- .-- . .-."

        actual_output = encryption(input_phrase)

        self.assertEqual(actual_output, expected_output)

    # Test invalid input (special characters)
    def test_encryption_invalid_input(self):
        """
        Test that encryption() handles invalid input containing special characters, returning None and not attempting to convert them.
        """
        input_phrase = "hello$%^&*"
        expected_output = None

        actual_output = encryption(input_phrase)

        self.assertEqual(actual_output, expected_output)

    # Test error handling (invalid input)
    def test_encryption_error_handling(self):
        """
        Test that encryption() raises a ValueError when given invalid input that cannot be converted to Morse code.
        """
        with self.assertRaises(ValueError):
            encryption('invalid_input')

    # Test handling of mixed-case letters
    def test_encryption_mixed_case_letters(self):
        """
        Test that encryption() correctly preserves the case of individual letters when converting a phrase with mixed-case letters.
        """
        input_phrase = "This Is A Mixed-Case Phrase"
        expected_output = "- .... .. ... / .-- .-. . -.- ... - / .- ..- -- .-.. .-.. .-.."

        actual_output = encryption(input_phrase)

        self.assertEqual(actual_output, expected_output)

    # Test handling of invalid input types (numbers, symbols)
    def test_encryption_invalid_input_types(self):
        """
        Test that encryption() raises a ValueError when given invalid input types, such as numbers or symbols.
        """
        invalid_inputs = [123, "@#$%", " "]
     # Test empty string
    def test_decryption_empty_string(self):
        """
        Test that decryption() returns an empty string when given an empty input string.
        """
        input_code = ""
        expected_output = ""

        actual_output = decryption(input_code)

        self.assertEqual(actual_output, expected_output)

    # Test simple code
    def test_decryption_simple_code(self):
        """
        Test that decryption() correctly decodes a simple Morse code representation to its corresponding English phrase.
        """
        input_code = "... . .-.. .-.. ---"
        expected_output = "hello"

        actual_output = decryption(input_code)

        self.assertEqual(actual_output, expected_output)

    # Test complex code
    def test_decryption_complex_code(self):
        """
        Test that decryption() correctly decodes a complex Morse code representation to its corresponding English phrase, including spaces.
        """
        input_code = "- .... .. ... / .--. .-. . -.- ... - / .-. .. ...- .-. .-.. ---"
        expected_output = "this is a test"

        actual_output = decryption(input_code)

        self.assertEqual(actual_output, expected_output)

    # Test mixed-case code
    def test_decryption_mixed_case_code(self):
        """
        Test that decryption() correctly handles Morse code representations with mixed-case letters, preserving the original case in the decoded phrase.
        """
        input_code = "..- .--. .--. . .-. / .-.. --- .-- . .-."
        expected_output = "UPPER lower"

        actual_output = decryption(input_code)

        self.assertEqual(actual_output, expected_output)

    # Test invalid input (extra characters)
    def test_decryption_invalid_input(self):
        """
        Test that decryption() handles invalid input containing extra characters, returning None and not attempting to decode them.
        """
        input_code = "... . .-.. .-.. --- abc..."
        expected_output = None

        actual_output = decryption(input_code)

        self.assertEqual(actual_output, expected_output)

    # Test error handling (invalid input)
    def test_decryption_error_handling(self):
        """
        Test that decryption() raises a ValueError when given invalid input that cannot be decoded from Morse code.
        """
        with self.assertRaises(ValueError):
            decryption('invalid_morse_code')

    # Test error handling (invalid characters)
    def test_decryption_error_handling_invalid_characters(self):
        """
        Test that decryption() raises a ValueError when given input containing invalid characters that are not part of the Morse code alphabet.
        """
        with self.assertRaises(ValueError):
            decryption('...--...---....')
