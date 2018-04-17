# ==. <>, !=, <, >, <=, >=, not, and, or

# score = 70
# if score >= 70:
#     print("good")
# else:
#     print("try harder")

def greeting(lang):
    if lang == "th":
        print("sawadee")
        print("สวัสสดี")
    elif lang == "jp":
        print("konochiwa")
    elif lang == "kr":
        print("ann-yeong")
    else:
        print("hello")
greeting("th")

def meet_req(eng, interview):
    if eng > 70 and interview > 70:
        return True
    else:
        return False

def meet_req2(eng, interview, math):
    if eng > 70 and interview > 70 and math >50:
        return True
    else:
        return False
print(meet_req(71,70))