from collections import defaultdict, namedtuple, Counter, deque
from datetime import datetime
import csv
import random
from urllib.request import urlretrieve

# In this Day 1 lesson we will use the most common collections types showing some easy to follow examples.
# Day 2 we will get some more practice using them on a movie data set.
# Day 3 we have you further practice using your own data.
# https://github.com/talkpython/100daysofcode-with-python-course/blob/master/days/04-06-collections/collections.ipynb

# A namedtuple is a convenient way to define a class without methods.
# This allows you to store dict like objects you can access by attributes.

# Let's first look at a classic tuple:
user = ('bob', 'coder')

print(f'{user[0]} is a {user[1]}')


# Now let's see a namedtuple
User = namedtuple('User', 'name role')
user = User(name='bob', role='coder')

print(user.name)
print(user.role)

print(f'{user.name} is a {user.role}')

# What about KeyError when using dict
users = {'bob': 'coder'}
users['bob']

# Gives us a key error
# users['julian']
#    users['julian']
# KeyError: 'julian'

# To get around the KeyError use get
users.get('bob')
if users.get('julian') is None:
    print('woops, no julian')

# What if you need to build up a collection?
challenges_done = [('mike', 10), ('julian', 7), ('bob', 5),
                   ('mike', 11), ('julian', 8), ('bob', 6)]
print(challenges_done)

# Key Error: 'mike'
# challenges = {}
# for name, challenge in challenges_done:
#     challenges[name].append(challenge)

challenges = defaultdict(list)
for name, challenge in challenges_done:
    challenges[name].append(challenge)

print(challenges)

# Counter
# Say you want the most common words in a text
words = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been 
the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and 
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into 
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum""".split()
print(words[:5])

# Before getting to know collections I would has written something like this:
common_words = {}
for word in words:
    if word not in common_words:
        common_words[word] = 0
    common_words[word] += 1

# sort dict by values descending and slice first 5 to get most common
for k, v in sorted(common_words.items(),
                   key=lambda x: x[1],
                   reverse=True)[:5]:
    print(k ,v)

# Now compare this to using Counter and its most_common method
print(Counter(words).most_common(5))

# Deques are a generalization of stacks and queues
# (the name is pronounced “deck” and is short for “double-ended queue”).
# Deques support thread-safe, memory efficient appends and pops from either side of the deque with
# approximately the same O(1) performance in either direction

# Lists in Python are awesome, probably one of your goto data structure, because they are so widely used and convenient.
# However certain operatings (delete, insert) can get slow when your list grows
# If you need to add/remove at both ends of a collection, consider using a deque.

# First we create two 10 million integers with range storing one in a list and the other in a deque
lst = list(range(10000000))
deq = deque(range(10000000))

# Let's do some removing and inserting at random locations in the sequence, a list is slow at this because
# it needs to move all adjacent around (Grokking Algorithms explains this really well).
# Here is where deque is a big win:

def insert_and_delete(ds):
    for _ in range(10):
        index = random.choice(range(100))
        ds.remove(index)
        ds.insert(index, index)

start = datetime.now()
insert_and_delete(lst)
end = datetime.now()

print(end - start)

start = datetime.now()
insert_and_delete(deq)
end = datetime.now()

print(end - start)

# So when performance matters you really want to explore the alternative data structures in the collections module.
#  Another example of a performance win is ChainMap:
#   A ChainMap groups multiple dicts or other mappings together to create a single, updateable view.
#   If no maps are specified, a single empty dictionary is provided so that a new chain always has at least one mapping.

# Let's make a defaultdict of movies per directory (keys = directors, values = list of movies).
movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
movies_csv = 'movies.csv'
urlretrieve(movie_data, movies_csv)

# A namedtuple is ideal here to describe a movie so we can access movie attributes (e.g. movie.score):
Movie = namedtuple('Movie', 'title year score')


# We need some CSV parsing as well here, no worries we got you covered:
def get_movies_by_director(data=movies_csv):
    """Extracts all movies from csv and stores them in a dictionary
       where keys are directors, and values is a list of movies (named tuples)"""
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors

directors = get_movies_by_director()

print(directors['Christopher Nolan'])

# You can do a lot with this data set and we challenge you to do so, but for this example let's just get the 5 directors with the most movies.

# Of course we don't want to re-invent the wheel so we use Counter:
cnt = Counter()
for director, movies in directors.items():
    cnt[director] += len(movies)

print(cnt.most_common(5))