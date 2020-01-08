#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for x in range(list_length):
        try:
            result = my_list_1[x] / my_list_2[x]
        except TypeError:
            print("{}".format("wrong type"))
            result = 0
        except ZeroDivisionError:
            print("{}".format("division by 0"))
            result = 0
        except IndexError:
            print("{}".format("out of range"))
            result = 0
        finally:
            new_list.append(result)
    return new_list
