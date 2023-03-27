#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        list2 = list()
        string = ''
        no_of_items = 0

        for i in range(my_list[0], my_list[x] - 1):
            list2.append(my_list[i])
            no_of_items += 1

        my_list = list2

#            string = ''.join([str(el) for el in my_list])
        return int(string), no_of_items
    except IndexError:
        return no_of_items
    except TypeError:
        return no_of_items
    else:
        string = ''.join(my_list)
        return int(string)


