import unittest

from morse_code import encription, decription

class TestEnglishPhrases(unittest.TestCase):

    def test_encription_english_phrases(self):
        """Tests the encription() function with English phrases."""

        # Test case 1
        input_phrase = "hello world"
        expected_output = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."

        actual_output = encription(input_phrase)
        

        # Test case 2
        input_phrase = "this is a test"
        expected_output = "- .... .. ... / .--. .-. . -.- ... - / .-. .. ...- .-. .-.. ---"

        actual_output = encription(input_phrase)


        # Test case 3 
        input_phrase= "help"
        expected_output= ".... . .-.. .-.. --- / -.-. --- .-. .-.."

        actual_output = encription(input_phrase)

        
        # Test case 4
        input_phrase= "S O S"
        expected_output="... / --- / ..."

        actual_output= encription(input_phrase)
        
        

        # Test case 5
        input_phrase= "UPPER lower"
        expected_output="..- .--. .--. . .-. / .-.. --- .-- . .-."

        actual_output= encription(input_phrase)

        # Test case 6
        input_phrase= "Give me the water"
        expected_output="--. .. ...- . / -- . / - .... . / .-- .- - . .-."

        actual_output= encription(input_phrase)
        
        

    def test_decription_english_phrases(self):
        """Tests the decription() function with English phrases."""

        # Test case 1
        input_code = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
        expected_output = "hello world"

        actual_output = decription(input_code)

        

        # Test case 2
        input_code = "- .... .. ... / .--. .-. . -.- ... - / .-. .. ...- .-. .-.. ---"
        expected_output = "this is a test"

        actual_output = decription(input_code)

       
        # Test case 3 
        input_code = ".... . .-.. .-.. --- / -.-. --- .-. .-.."
        expected_output = "help"

        actual_output= decription(input_code)

        
        
        # Test case 4
        input_code= "... / --- / ..."
        expected_output= "S O S"

        actual_output= decription(input_code)

       
        # Test case 5
        input_code= "..- .--. .--. . .-. / .-.. --- .-- . .-."
        expected_output= "UPPER lower"

        actual_output= decription(input_code)

        # Test case 6
        input_code= "--. .. ...- . / -- . / - .... . / .-- .- - . .-."
        expected_output= "Give me the water"

        actual_output= decription(input_code)


        


if __name__ == "__main__":
    unittest.main()