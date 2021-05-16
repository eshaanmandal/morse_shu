# Morshu

<p>Morshu is a python library that helps you to work with morse codes. What makes it different? </p>

- Implemented with classes
- Programmers can change separators between characters and words
- It is named after <b><i>Morshu</i></b>


## Basic morse code encoding and decoding
```python
import morshu

m = morshu.Morse()
text = 'lamp oil rope bomb you want it'
print(m.convert_to_morse(text))
coded_msg = m.convert_to_morse(text)
print(m.convert_to_normal_text(coded_msg))
```
### this will give the output

```
.-.. .- -- .--.   --- .. .-..   .-. --- .--. .   -... --- -- -...   -.-- --- ..-   .-- .- -. -   .. - 
lamp oil rope bomb you want it
```
