a_dict = {'server': 'db.diveintopython3.org', 'database': 'mysql'}
print(a_dict)
print(a_dict['server'])
print(a_dict['database'])
a_dict['database'] = 'blog'
print(a_dict)
a_dict['user'] = 'dora'
print(a_dict)
a_dict['user'] = 'haoliang'
print(a_dict)
print(a_dict.get('user'))
print(a_dict.get('people'))
a_dict['User'] = 'mark'
print(a_dict)
