# Lab Session - 1

### Installing nltk
Install nltk package using `pip install nltk`.
You'll then need to download the NLTK corpuses.
```python
# To download all the nltk corpus
import nltk
nltk.download()
```

```markdown
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908
```

### Concordance View
A concordance view present the given word along with some related context so as to make the meaning and usage of the word clear.

```python
from nltk.book import text1
# Concordance views show us every occurence of a given word, together with some context
text1.concordance("crooked")

# Displaying 8 of 8 matches:
# rcing serpent , even Leviathan that crooked serpent ; and he shall slay the dra
#  we met where the place was : these crooked directions of his very much puzzled
# , the key - hole prospect was but a crooked and sinister one . I could only see
# ed whale with a wrinkled brow and a crooked jaw ; whosoever of ye raises me tha
# he mention of the wrinkled brow and crooked jaw they had started as if each was
# or Moby Dick ?" " I am game for his crooked jaw , and for the jaws of Death too
# at every dart , hauling in upon his crooked lance ( by the line attached to it 
# here were plainly revealed two long crooked rows of white , glistening teeth ,
```
