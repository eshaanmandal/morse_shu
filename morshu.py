class Morse:
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
    def __init__(self, char_separator=' ', space_separator='  ', dictionary=None):
        self.char_separator = char_separator
        self.space_separator = space_separator
        if dictionary is None:
            self.dictionary = Morse.morse_codes
        else:
            self.dictionary = dictionary


    def convert_to_morse(self, string='hello world'):
        self.coded_string=''
        l_string = string.lower()
        for char in l_string:
             if char in self.dictionary.keys():
                 self.coded_string += self.dictionary[char] + self.char_separator
             else:
                  self.coded_string += self.space_separator
        
        return self.coded_string

    def convert_to_normal_text(self, string= '.... . .-.. .-.. ---   .-- --- .-. .-.. -.. '):
        space_num = len(self.space_separator) + len(self.char_separator)

        clean_code = ''  
        for char in string:
            if char not in self.dictionary.keys():
                clean_code += ' ' 
            else:
                clean_code += char
  
        self.normal_text, citext = '',''
        spaces=0
        for c in clean_code:
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

                
                


