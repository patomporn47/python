def raectange(w, h): #dynamic typing
    #code block
    area = w * h
    return area
def triangle(w, h):
    # area = .5 * w * h
    return .5 * w * h
# main entry point
print("1. raectange")
print("2. triangle")
n = input("please select option: ")
w = int(input("width = "))
h = int(input("height = "))
if n == "1":
    print("raectange area")
    print(raectange(w, h))
else:
    print("triangle area")
    print(triangle(w, h))

