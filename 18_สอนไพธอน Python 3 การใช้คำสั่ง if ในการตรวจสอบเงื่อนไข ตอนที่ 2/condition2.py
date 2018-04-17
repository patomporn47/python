def ticket(age):
    if age <= 5 :
        return 0
    else:
        return 100


def ticket2(age):
    if age <= 5 or age >= 60 :
        return 0
    else:
        return 100

def ticket2a(age):
    return 0 if age <= 5 or age >= 60 else 100 #ternary



def ticket3(age, is_local):
    if (age <= 5 or age >= 60) and is_local:
        return 0
    else:
        return 100

def ticket3a(age, is_local):
    return 0 if (age <= 5 or age >= 60) and is_local else 100
    #     return 0
    # else:
    #     return 100

# print(ticket(4))
# print(ticket2(70))
# print(ticket2(35))
# print(ticket2(3))
# print(ticket3(3,True))
# print(ticket3a(4,False))

def demo(a):
    if a >= 10 and a <= 20 :
        print("ok")
    else:
        print("not ok")


def demo2(a):
    if 10 <= a <= 20 :
        print("ok")
    else:
        print("not ok")

demo(118)
demo2(118)
