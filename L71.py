#The author is Aliza Litvak

def too_long(x):
    if len(x)>140:
        print ("too many characters")
    if len(x)<=140:
        print ("sent")

too_long("hello")
