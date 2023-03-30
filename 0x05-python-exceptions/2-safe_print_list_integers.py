#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    list2 = list()
    count = 0
    try:
        for i in range(0, x):
           if (all(type(my_list[i]) in [int] for i in my_list)):
               raise TypeORvalue
    except TypeORvalue:
        for j in range(0, x):
            if (type(my_list[i]) == int):
                list2.append(str(my_list[i]))
                count += 1
        stri = ''.join(list2)
        inte = int(stri)
        print(inte)
        return count
    else:

        for j in range(0, x):
            list2.append(str(my_list[i]))
            count += 1
        stri = ''.join(list2)
        inte = int(stri)
        print(inte)
        return count

