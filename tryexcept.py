import random

e = ['http://www.google.com', 'http://www.amazon.com', 'http://www.facebook.com', 'http://www.cnn.com', 'http://www.nytimes.com']
g = random.sample(list(enumerate(e)), k = 2)
r = [h[0] for h in g]

print(r)
