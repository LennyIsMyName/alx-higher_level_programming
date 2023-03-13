#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        fir = tuple_a[0] + tuple_b[0]
        sec = tuple_a[1] + tuple_b[1]
        new = (fir, sec)
        return new
    else:
        tuplist1 = list(tuple_a)
        tuplist2 = list(tuple_b)
        if len(tuplist1) == 1:
            tuplist1.append(0)
        if len(tuplist2) == 1:
            tuplist2.append(0)
        if len(tuplist1) == 0:
            tuplist1.append(0)
            tuplist1.append(0)
        if len(tuplist2) == 0:
            tuplist2.append(0)
            tuplist2.append(0)
        fir = tuplist1[0] + tuplist2[0]
        sec = tuplist1[1] + tuplist2[1]
        new = (fir, sec)
        return new
