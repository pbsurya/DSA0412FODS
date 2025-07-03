import matplotlib.pyplot as plt
from collections import Counter
import string
from wordcloud import STOPWORDS

feedbacks = [
    "Love the product and the price was good",
    "Very useful and helpful service",
    "Good value for money",
    "Not satisfied with the quality",
    "Excellent product, fast delivery"
]

# Preprocess and gather all words
all_words = []
for feedback in feedbacks:
    text = feedback.lower().translate(str.maketrans('', '', string.punctuation))
    all_words.extend([word for word in text.split() if word not in STOPWORDS])

# Frequency Distribution
freq_dist = Counter(all_words)
top_words = freq_dist.most_common(5)

# Plot
words, counts = zip(*top_words)
plt.bar(words, counts)
plt.title("Top 5 Frequent Words in Feedbacks")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.show()
