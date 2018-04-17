def celsius_to_fah(celsius):
    return (celsius * 9 / 5) + 32

def temperature_table(): # void fouction in C, Java
    for c in range(0, 101, 5):
        f = celsius_to_fah(c)
        print("{}C = {}F".format(c, f))
    #return None

def menu():
    print("1. convert Celsius to Fahrenheit")
    print("2. diskplay temperature table")
    n = input("enter choice: ")
    if n == "1":
        celsius = float(input("enter degree in Celsius: "))
        print("{}C = {}F".format(celsius, celsius_to_fah(celsius)))
    elif n == "2":
        temperature_table()
    else:
        print("WTF")

# f = celsius_to_fah(100)
# print(f)
# temperature_table()
# a = temperature_table()
# print(a)
menu()