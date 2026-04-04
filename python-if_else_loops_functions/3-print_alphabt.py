#!/usr/bin/python3
print("".join(["{:c}".format(97 + i) for i in range(26)
               if chr(97 + i) != 'q' and chr(97 + i) != 'e']), end="")
