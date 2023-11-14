#creating a variable containing dictionary taking alphabet as key, morse code as value

key_alphabet= {"a": ".-","b": "-...","c": "-.-.","d": "-..","e": ".","f": "..-.",
               "g": "--.","h": "....","i": "..","j": ".---","k": "-.-","l": ".-..",
               "m": "--","n": "-.","o": "---","p": ".--.","q": "--.-","r": ".-.",
               "s": "...","t": "-","u": "..-","v": "...-","w": ".--","x": "-..-","y": "-.--","z": "--..",
               "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
               "H": "...", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-", "O": "---", "P": ".--.",
               "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--.."}
key_alphabet[" "] = "/" #adding a key for the space character in the key_alphabet dictionnary 

#creating a variable containing dictionary taking morse code as key, alphabet as value

key_morsecode = { ".-": "a",  "-...": "b",  "-.-.": "c",  "-..": "d",  ".": "e",  "..-.": "f",  "--.": "g",
                   "....": "h",  "..": "i",  ".---": "j",  "-.-": "k",  ".-..": "l","--": "m" , "-.": "n",
                  "---": "o", ".--.": "p","--.-": "q",".-.": "r","...": "s", "-": "t","..-": "u", "...-": "v",
                  ".--": "w","-..-": "x",  "-.--": "y","--..": "z" ,"/": " "," ": "+",".-": "A", "-...": "B", "-.-.": "C", "-..": "D",
                  ".": "E", "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
                  ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y", "--..": "Z"}

#function encrypt phrase to morse code

def encription(phrase):
    """Phrase is converted to morse code.

    Parameter:
            phrase:string input containing phrase to encrypt.

    Return:string output containing encrypted version of the phrase.

    """
    encrypt = ""
    for letter in phrase:
        encrypt+= key_alphabet[letter] + " "
    return encrypt

#function decrypt a morse code to English

def decription(code):
    """code is converted to English phrase.

    Parameter:
             code=String input containg morse code to decrypt.

    Return:string output containing decrypted version of the code.

    """
    decrypt = ""
    current_morse = ""
    for character in code:
        if character != " ":
            current_morse += character
        else:
            if current_morse:
                 decrypt += key_morsecode[current_morse]
            current_morse = ""
    if current_morse:
        decrypt += key_morsecode[current_morse]
    return decrypt

#function encrypting/decrypting a given input

def test():
    """asks the user about an input and wether to decrypt or encrypt it.

    Parameters:
             input:String input containing a morse code or a phrase.
             Method:asks the user to encrypt or decrypt the input.
    
    Return:String output containing encrypted/decrypted version of the initial input.

    """ 
    method=input("please enter encrypt or decrypt :")
    input_user=input("please enter your input :")
    final_result=""
    if method=="encrypt":
         for letter in input_user:
            if not letter.isalpha():
               print("Invalid input: Numbers are not allowed")
               return ""
         final_result=encription(input_user)
         print("the encrypted version is:",final_result)
    elif method=="decrypt":
            final_result=decription(input_user)
            print("the decrypted version is:",final_result)
    else:
         print("u have entered a wrong method,try again with encrypt or decrypt")

    return final_result
c=test()
print(c)
