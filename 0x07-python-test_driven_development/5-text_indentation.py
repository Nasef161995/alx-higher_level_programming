#!/usr/bin/python3
"""text_indentation
"""

def text_indentation(text):
    """text_indentation
    arg:
        text: text
    """
    if not isinstance(text, str):
            raise TypeError("text must be a string")
    for i in text:
        if (i == '.' or i == '?' or i == ':') :
            print(i)
            print()
        else:
            print(i.strip(), end='')
