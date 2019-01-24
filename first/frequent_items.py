from collections import Counter
text = "I'm selfish, impatient and a little insecure." \
       "I make mistakes, I am out of control and at times hard to handle." \
       "But if you can't handle me at my worst, then you sure as hell don't deserve me at my best. "

words = text.split()
print(words)

counter = Counter(words)
top_three = counter.most_common(10)
print(top_three)
