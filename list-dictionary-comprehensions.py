from typing_extensions import LiteralString


list = list(range(100))

list1 = [5*item for item in list if item % 2 == 0]

print(list1)

string = "Bring and place it on the table. Do not touch anything."

print(string.split())


def cleanWords(word) -> LiteralString:
    return word.replace(".",'').lower()

print([cleanWords(word) for word in string.split() if len(cleanWords(word))>2])

print(2**9 / 1.4)

animalList = [('a','aardvark'),('b','bear'),('c',['cat','coyote'])]
animals = {item[0]: item[1] for item in animalList}
print(animals)

# unpacking tuples into key, value vars
animals = {key: value for key, value in animalList}
print(animals)
print(animals.items())
print([{'letter': key, "name": value} for key,value in animals.items()])

dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.keys()
values = dishes.values()

print(type(range(10)))