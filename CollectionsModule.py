from collections import Counter
from collections import defaultdict
from collections import namedtuple

# Example of Counter Class
letters = 'aaaaaaaabbbbbbacccccccddddddddddddddddddddddddd'

c = Counter(letters)

print(c)
print(c.most_common())
print(list(c))


# Example of defaultdict to not get error while indexing wrong key in dictionary
d = defaultdict(lambda: 0)

d['correct'] = 100
print(d['wrong'])

print(d)

# Example of namedtuple
Dog = namedtuple('Dog', ['age', 'breed', 'name'])
Sammy = Dog(age = 5, breed = 'Husky', name = 'Sammy')

print(Sammy)