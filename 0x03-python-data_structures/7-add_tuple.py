#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        fir = tuple_a[0] + tuple_b[0]
        sec = tuple_a[1] + tuple_b[1]
        new = (fir, sec)
        return new
    else:
        fir = tuple_a[0] or 0 + tuple_b[0] or 0
        sec = tuple_a[1] or 0 + tuple_b[1] or 0
        new = (fir, sec)
        return new
