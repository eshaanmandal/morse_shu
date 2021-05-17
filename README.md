# Morse_shu - the morse code module

Morshu (pronounced as more-shoe) is a python module which helps the programmer in generating morse codes, decoding them, etc.

- Implemented with classes
- Programmers can define separators between characters and words
- It is named after <b><i>Morshu</i></b>


## Installation
Just download and paste morshu.py where your python modules are present or in the directory where your current program is present

## Usage 

### Using the predefined character separator and space separator
```python
import morshu


m = morshu.Morse(space_separator='  ', char_separator=' ')

text_message = '''Lamp oil, rope, bombs, you want it?'''

try:
    m.convert_to_morse(text_message)
    print(m.coded_string)
    m.convert_to_normal_text(m.coded_string)
    print(m.normal_text)
except AttributeError:
    print(m.error_message)
```
```
.-.. .- -- .--.  --- .. .-..    .-. --- .--. .    -... --- -- -... ...    -.-- --- ..-  .-- .- -. -  .. - ----
lamp oil rope bombs you want it?
```
### Using character separator and space separator given by the user
```python
import morshu


m = morshu.Morse(space_separator=' # ', char_separator='$')

text_message = '''Lamp oil, rope, bombs, you want it?'''

try:
    m.convert_to_morse(text_message)
    print(m.coded_string)
    m.convert_to_normal_text(m.coded_string)
    print(m.normal_text)
except AttributeError:
    print(m.error_message)
```

```
.-..$.-$--$.--. # ---$..$.-.. #  # .-.$---$.--.$. #  # -...$---$--$-...$... #  # -.--$---$..- # .--$.-$-.$- # ..$-$---- # 
lamp oil rope bombs you want it?
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
