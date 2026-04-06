#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Açarları əlifba sırası ilə sıralayırıq
    sorted_keys = sorted(a_dictionary.keys())

    # Sıralanmış açarlar üzrə dövr (loop) qurub çap edirik
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
