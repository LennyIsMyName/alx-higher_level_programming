#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        list2 = list()
        count = 0
        for i in range(x):
            list2.append(str(my_list[i]))
            count += 1
        string = ''.join(list2)
        print(string)
    except IndexError:
        count = 0
        listE = list()
        for i in my_list:
            listE.append(str(i))
            count += 1
        stringE = ''.join(listE)
        print(stringE)

    finally:
        return count
