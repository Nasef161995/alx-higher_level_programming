#!/usr/bin/python3
a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
print(a_dictionary.values())
print(a_dictionary["John"])
#new = {key: for key in a_dictionary.kays() val*2  for val in a_dictionary.values(), for item in a_dictionary.items()}

items = a_dictionary.items()

a=[(key, val*2) for key, val in items]

new = dict(a)



print(new)
