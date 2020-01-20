#!/usr/bin/python3
'''class MyList that inherits from list'''


class MyList(list):
    '''class that inherits from list'''
    def print_sorted(self):
        '''method that prints the list, but sorted (ascending sort)'''
        print(sorted(self))
