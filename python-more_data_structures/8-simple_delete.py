#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Açarı silməzdən əvvəl onun lüğətdə olub-olmadığını yoxlayırıq
    if key in a_dictionary:
        del a_dictionary[key]

    return a_dictionary
