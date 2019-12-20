#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        newdic = a_dictionary.copy()
        biggest = 0
        for i in newdic:
            if newdic[i] > biggest:
                biggest = newdic[i]
                bestscore = i
        return bestscore
