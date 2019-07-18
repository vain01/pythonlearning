import string

c = "  I am liang."
print(c)
print(c.strip(string.punctuation + string.whitespace))
