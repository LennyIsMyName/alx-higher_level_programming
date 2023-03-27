#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        list2 = list()
        count = 0
        counti = 0
        for item in my_list:
            counti += 1
        for i in range(0, x):
            list2.append(str(my_list[i]))
            count += 1
        string = ''.join(list2)
        inte = int(string)
    except IndexError:
        countE = 0
        listE = list()
        for i in range(0, countE):
            list2.append(str(my_list[i]))
        stringE = ''.join(listE)
        intE = int(stringE)
        return intE
    except TypeError:
        pass
    except ValueError:
        pass
    except:
        pass
    else:
        print(inte)
    finally:
        return count
