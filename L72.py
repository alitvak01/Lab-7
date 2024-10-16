#The authors is Aliza Litvak

def o_s(word):
    total = 0
    for x in word:
        if x == "o":
            total = total + 1
    return total

o_s("bonobos")
