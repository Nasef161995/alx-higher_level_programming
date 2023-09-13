#!/usr/bin/python3
a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
a = a_dictionary.items()
n = [(key, val) for key, val in a_dictionary.items() if val != "c"]



print(n)
