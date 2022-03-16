#!/usr/bin/python

def lucky_8(a,b):
    if a==8 or b==8:
        return True
    elif a+b==8:
        return True
    elif a-b==8 or b-a==8:
        return True
    else:
        return False

a = int(input("Please enter first number: "))
b = int(input("Please enter second number: "))
check_luck = lucky_8(a,b)
print(f"you are a {check_luck} winner")
