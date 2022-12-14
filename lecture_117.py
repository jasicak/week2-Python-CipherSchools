# dictionaries intro
# unordered collections of data in key : value pair
user = {'name' : 'Jasica', 'age' : 18}
print(user)
print(type(user))

# another method

user1=dict(name='Jasica', age=18)
print(user1)

# how to access data from dictionary

print(user['name'])
print(user['age'])

user_info={
    'name' : 'Jasica',
    'age' : 24,
    'fav_colours' : ['red', 'orange'],
    'fav_fruits' : ['apple', 'kiwi'],
    }
print(user_info['fav_fruits'])

#how to add data to empty dictionary

user_info2={}
user_info2['name'] = 'Jasica'
print(user_info2)
