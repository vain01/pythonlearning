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
