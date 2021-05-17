class Morse:
    '''the default dictionary used for encoding and decoding '''
    morse_codes = {
    't':'-', 'e':'.',
    'm':'--', 'n':'-.',
    'a':'.-', 'i':'..',
    'o':'---', 'g':'--.',
    'k':'-.-', 'd':'-..',
    'w':'.--', 'r':'.-.',
    'u':'..-', 's':'...',
    '?':'----', '.':'---.',
    'q':'--.-', 'z':'--..',
    'y':'-.--', 'c':'-.-.',
    'x':'-..-', 'b':'-...',
    'j':'.---', 'p':'.--.',
    'l':'.-..', '-':'..--',
    'f':'..-.', 'v':'...-',
    'h':'....', '0':'-----',
    '9':'----.', '8':'---..',
    '7':'--...', '6':'-....',
    '1':'.----', '2':'..---',
    '3':'...--', '4':'....-',
    '5':'.....'
}
    error_message = ''
    error_code = 0
    def __init__(self, char_separator=' ', space_separator='  ', dictionary=None):
        ''' The default constructor accepts the character to use to differentiate between
            characters and words, default values are single space and double space, the dictionary
            used for encoding/decoding '''
        if len(char_separator) > len(space_separator):
            self.error_code = -1
            self.error_message = '''The length of space separator is less than character separator, it may lead to additional problems when decoding'''

        self.char_separator = char_separator
        self.space_separator = space_separator
        if dictionary is None:
            self.dictionary = Morse.morse_codes
        else:
            self.dictionary = dictionary


    def convert_to_morse(self, string):
        ''' Method converts normal text to morse code '''
        if self.error_code == -1:
            return 

        char_count = 0 # Counts the number of character iterated by the for loop
        string = string + ' ' # adds a space after the last character else it doesn't get encoded to morse
        isfirstchar  = True # flag for checking if the the character is the first character of a word
        coded_char ='' # stores the encoded character
        self.coded_string='' # the final encoded string that would be returned
        l_string = string.lower() # converts the text into lower case
        for char in l_string:
             if char in self.dictionary.keys():
                 char_count += 1

                 if char_count == 1:
                     if isfirstchar:
                        coded_char += self.dictionary[char]
                        isfirstchar = False
                     else:
                         coded_char += self.char_separator
                         coded_char +=self.dictionary[char]
                 elif char_count == 2:
                     self.coded_string += coded_char
                     self.coded_string += self.char_separator
                     self.coded_string += self.dictionary[char]
                     char_count = 0
                     coded_char = ''
             else:

                 isfirstchar = True
                 coded_char += self.space_separator
                 self.coded_string += coded_char
                 char_count = 0
                 coded_char = ''
                  
        
        return self.coded_string

    def convert_to_normal_text(self, string):
        ''' Converts the morse code to normal text'''
        if self.error_code == -1:
            return 

        string = string + ' ' # a space is needed after the last char else the method fails at last char
        # /t is of len 1 which causes certain problems: this conditional is for dealing with that

        if '\t' in self.space_separator:
            space_num = len(self.space_separator) + 1
        else:
            space_num = len(self.space_separator) 

        # cleaning the code from all the separators after this the code only contains spaces between the characters
        self.clean_code = ''  
        for char in string:
            if char not in self.dictionary.keys() and char == '\t':
                self.clean_code += '  '
            elif char not in self.dictionary.keys() and char != '\t':
                self.clean_code += ' '
            else:
                self.clean_code += char
     
        self.normal_text, citext = '',''
        spaces = 0 # counts the number of spaces
        # conversion begins
        for c in self.clean_code:
            if c != ' ':
                spaces = 0
                citext += c

            else:
                spaces += 1
                if spaces == space_num:
                    self.normal_text += ' '

                elif spaces == 1:
                    self.normal_text += list(self.dictionary.keys())[list(self.dictionary.values()).index(citext)]
                    citext = ''
    
        return self.normal_text

