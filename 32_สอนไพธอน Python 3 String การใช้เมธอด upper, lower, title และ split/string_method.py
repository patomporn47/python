# s = "peter"
# print(s.capitalize())
# print(s.upper())
# t = "PARKER"
# print(t.lower())
def demo_upper():
    choice = input("[M]ale, [F]emale: ")
    if choice.upper() == "M":
    # if choice == "M" or choice == "m":
        print("male")
    elif choice.upper() == "F":
    # if choice == "M" or choice == "m":
        print("female")

    else:
        print("fuck")

def demo_title():
    s = "the land of smiles"
    print(s.title())

demo_title()