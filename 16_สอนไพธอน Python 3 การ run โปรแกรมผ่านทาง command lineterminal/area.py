def raectange(w, h): #dynamic typing
    #code block
    area = w * h
    return area
def triangle(w, h):
    # area = .5 * w * h
    return .5 * w * h
# main entry point
w = int(input("width = "))
h = int(input("height = "))
# print(raectange(w, h))
print(triangle(w, h))