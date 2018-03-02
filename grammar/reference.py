print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
print('shoplist is', shoplist)
mylist = shoplist
print('mylist is', mylist)
del shoplist[0]
print('shoplist is now', shoplist)
print('mylist is now', mylist)

print('Copy by making a full slice')
mylist = shoplist[:]
del mylist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)
