# PySynonym
PySynonym is a plugin that returns a list of synonyms for the given word. This is very useful when programming bots and digital assistants, to increase their understanding.

## How to use PySynonym <br>
<b>Installation:</b> `pip install PySynonym` <br>
<b>Including:</b> `import PySynonym as ps` <br>
<b>Finding synonyms:</b> `ps.synonym('word')` <br>
<b>Finding definitons:</b> `ps.explain('word')` <br>

## Example code <br>
```python
import PySynonym as ps

syn = ps.synonym('house')
if 'building' in syn:
    print("Building is a synonym of house")
else:
    print("Building is no synonym of house")
```
Advanced example using nltk processing:
```python
import PySynonym as ps
import nltk

string = "Please turn on the light"
sentence = nltk.word_tokenize(string)

if len(set(sentence) & set(ps.synonym('lamp'))) > 0:
    print("Turn the lamp on")

```
The command to turn on the light is being split into words using nltk. Then the list of tokens is being compared to the list of synonyms of 'lamp' to see if it matches. If yes, the light is being turned on.