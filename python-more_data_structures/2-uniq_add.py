#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Listi set-ə çeviririk ki, yalnız unikal elementlər qalsın
    unique_numbers = set(my_list)

    # Bu unikal elementlərin cəmini hesablayırıq
    total_sum = sum(unique_numbers)

    return total_sum
