# Encryption and decryption

A user friendly python program,the user simply enters the message in the application and choose to encrypt or decrypt.

##table of contents:
-[Installation](#intallation)
-[how to use](#how-to)
-[examples](#examples)
-[Key components](#key-components)
-[Contributing](#contributing)

#installation 

-simply clone this repository and run the following command: python setup.py install

##how to use

-To encrypt a message, run the following command: python morse_code.py encript <message>
-To decrypt a Morse code message, run the following command: python morse_code.py decript <morse_code_message>

##examples

-To encrypt the message "hello world", run the following command:
python morse_code.py encript hello world
This will print the following output:.... . .-.. .-.. --- / .-- --- .-. .-.. -..
-To decrypt the Morse code message ".... . .-.. .-.. --- / .-- --- .-. .-.. -..", run the following command:
python morse_code.py decript .... . .-.. .-.. --- / .-- --- .-. .-.. -..
This will print the following output:hello world

##key components

The following are some of the key components of the Morse code application:
-encryption() = This function encrypts a message using Morse code.
-decryption() = function decrypts a Morse code message.
-key_alphabet= {} = variable containing dictionary taking alphabet as key, morse code as value
-key_morsecode = {} = variable containing dictionary taking morse code as key, alphabet as value

##contributing

If you would like to contribute to the Morse code application, please fork this repository and create a pull request.

