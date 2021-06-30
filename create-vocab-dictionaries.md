Note: Won't work on languages like Chinese in which there is no space between words.

```Python
unique_words = list(set(text.split(' ')))
word_to_index = {k:v for (v,k) in enumerate(unique_words)}
index_to_word = {v:k for (v,k) in enumerate(unique_words)}



```
