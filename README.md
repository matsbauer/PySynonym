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