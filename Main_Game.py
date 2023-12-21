import os
from Logika import *

os.system('cls')

w1 = " "
w2 = " "
w3 = " "
w4 = " "
w5 = " "
w6 = " "
w7 = " "
w8 = " "
w9 = " "

i = 0
while True:
    if i == 5:
        break
    w1, w2, w3, w4, w5, w6, w7, w8, w9 = Wybor(w1, w2, w3, w4, w5, w6, w7, w8, w9)

    os.system('cls')
    
    print(w1,"|",w2,"|",w3)
    print("__________")
    print(w4,"|",w5,"|",w6)
    print("__________",)
    print(w7,"|",w8,"|",w9,)
    i += 1
