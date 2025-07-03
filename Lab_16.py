from collections import Counter
import string
from wordcloud import STOPWORDS

reviews = """
This product is excellent. The quality is very good and the price is reasonable.
Excellent product and very satisfied. Will recommend to others.
"""

# Preprocessing
reviews = reviews.lower().translate(str.maketrans('', '', string.punctuation))
review_words = reviews.split()
filtered_words = [word for word in review_words if word not in STOPWORDS]

freq = Counter(filtered_words)

print("Review Word Frequency:", freq.most_common(10))
