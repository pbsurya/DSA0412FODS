from collections import Counter
import string

text = """
Natural language processing (NLP) is a field of artificial intelligence that enables computers to understand, interpret, and generate human language.
"""

# Preprocessing
text = text.lower().translate(str.maketrans('', '', string.punctuation))
words = text.split()
freq = Counter(words)

print("Word Frequency:", freq.most_common(10))
