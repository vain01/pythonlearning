shoplist = ['apple', 'mango', 'carrot', 'banana']
print('I have', len(shoplist), 'items to purchase.')
print('These items are:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nI also to buy rice')
shoplist.append('rice')
print('Shoplist is now', shoplist)
shoplist.sort()
print('Shoplist is sorted', shoplist)
print('The 1st item I will buy is', shoplist[0])
old_item = shoplist[0]
del shoplist[0]
print('I bought the', old_item)
print('My shoplist is now', shoplist)
