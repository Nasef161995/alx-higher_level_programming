#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        result = fct


    except (TypeError, ValueError) as error:
        print("Exception:", error)



    return result
