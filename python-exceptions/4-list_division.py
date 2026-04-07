#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        res = 0
        try:
            # Bölmə əməliyyatını yoxlayırıq
            res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            # Hər bir halda nəticəni (və ya 0-ı) yeni listə əlavə edirik
            new_list.append(res)
    return new_list
