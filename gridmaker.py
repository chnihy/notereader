#! python3
# grid maker - a program to make musical grid exercises
from copy import copy 

def MovingGrid(a, b, subdiv):
    lst = []
    for i in range(subdiv):
        lst.append(a)
    for i in range(len(lst)):
        lst2 = copy(lst)
        lst2[i] = b
        print(lst2)

def StackingGrid(a, b, subdiv):
    lst = []
    for i in range(subdiv):
        lst.append(a)
    for i in range(len(lst)):
        lst[i] = b
        print(lst)

def ReversingGrid(a, b, subdiv):
    lst = []
    for i in range(int(subdiv/2)):
        lst.append(a)
        lst.append(b)
    print(lst)
    print(lst[::-1])

print("Moving Grid: ")
MovingGrid("bed","VAR",8)

print("Stacking Grid: ")
StackingGrid("bed", "VAR", 8)

print("Reversing Grid: ")
ReversingGrid("bed", "VAR", 8)