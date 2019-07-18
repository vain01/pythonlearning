import random

characters = list()

characters.append("a")
characters.append(["a", "8"])
characters.append(("4",))

characters.extend(["b", "c"])
characters.extend(("0",))
characters.extend("A")

print(characters)

characters.insert(0, "AA")

print(characters)

characters.insert(0, characters.pop(-1))

print(characters)

names = ['China', 'ShanDong', 'Shanghai', 'Aabo']
name = names[random.randint(0, len(names))]
print(name)
name = names[-1]
print(name)
name = names.__getitem__(0)
print(name)
