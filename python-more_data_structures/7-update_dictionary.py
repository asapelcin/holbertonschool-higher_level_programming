#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # Python lüğətlərində bu əməliyyat çox sadədir:
    # Əgər key varsa yeniləyir, yoxdursa yeni əlavə edir.
    a_dictionary[key] = value
    return a_dictionary
