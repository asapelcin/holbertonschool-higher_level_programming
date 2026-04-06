#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Orijinal lüğəti dəyişməmək üçün yeni lüğət yaradırıq
    new_dict = {}

    # Lüğətin içindəki hər bir açar-dəyər cütü üzərində gəzirik
    for key, value in a_dictionary.items():
        # Dəyəri 2-yə vurub yeni lüğətə əlavə edirik
        new_dict[key] = value * 2

    return new_dict
