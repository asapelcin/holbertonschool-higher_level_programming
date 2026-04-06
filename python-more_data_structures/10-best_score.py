#!/usr/bin/python3
def best_score(a_dictionary):
    # Əgər lüğət boşdursa və ya daxil edilməyibsə None qaytarırıq
    if not a_dictionary:
        return None

    # Max() funksiyasından istifadə edərək ən böyük dəyərə (value) sahib açarı tapırıq
    # key=a_dictionary.get hissəsi lüğəti dəyərlərə görə müqayisə etməyə imkan verir
    return max(a_dictionary, key=a_dictionary.get)
