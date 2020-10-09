bag=dict()
bag['pants']=12
bag['sneakers']=75
bag['computer']=4
print(bag)

# basically an object
# {'pants': 12, 'sneakers': 75, 'computer': 4}
# use in operator to check if key is in dictionary

# get() if key exists, prints value, else prints default (here 0)
print(bag.get('pen',0))
print(bag.get('sneakers',0))

# double iteration variables
for name, value in bag.items():
    print(name, value)