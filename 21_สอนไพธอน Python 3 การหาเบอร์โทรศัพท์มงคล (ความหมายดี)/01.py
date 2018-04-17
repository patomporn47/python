def sum_phone_digit(phone_number):
    total = 0
    for c in phone_number:  # "0813451234"
        total += int(c)
    return total
# print(sum_phone_digit("0866056995"))
print(sum_phone_digit("9999999999"))