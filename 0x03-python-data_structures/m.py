#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        a = tuple_a[0] = 0
        b = tuple_a[1] = 0
    elif len(tuple_b) == 0:
        c = tuple_b[0] = 0
        d = tuple_b[1] = 0
    elif len(tuple_a) == 1:
        b = tuple_a[1] = 0
    elif len(tuple_b) == 1:
        d = tuple_b[1] = 0
    else:
        a = tuple_a[0]
        b = tuple_a[1]
        c = tuple_b[0]
        d = tuple_b[1]

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])



    
    
    
    
    
    
    
    
    
   
        
