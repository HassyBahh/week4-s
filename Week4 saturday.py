print("welcome to saturday class week4")
print(5>3)
print(5<3)
print(5==3)
print(5==5)
print(5!=3)
print("apple" < "banana")

#Variables
age = 20
is_girl= True
raining = False
score = 69

#learning about IF statement
#and condition
if age >= 20 and is_girl:
    print("na for yarn am ")
if age <= 19 and is_girl:
    print("na for yarn am ")

#or condition
if age >=20 or is_girl:
    print("na for yarn am ")
if age <=20 or is_girl:
    print("na for yarn am ")

#not condition
if not raining:
    print("Go outside ")

#SINGLE IF STATEMENT
if score >= 50:
    print("You pass")

#learning about ELSE
if score >= 50:
    print("You pass")
else :
    print("You fail")

#learning about ELIF
if score >= 90:
    print(" A")
elif score >= 80 or score >= 89:
    print("B")
elif score >= 70 or score >= 79:
    print("C")
elif score >= 60 or score >= 69:
    print("D")
else:
    print("F")

#learning about NESTED IF
if score >= 90:
    print(" A")
    if score ==91:
        print("u get 91")
    elif score ==92:
        print("u get 92")

elif score >= 80 or score >= 89:
    print("B")
    if score == 83:
        print("u get 83")
    elif score == 84:
        print("u get 84")

elif score >= 70 or score >= 79:
    print("C")
    if score ==74:
         print("u get 74")
    elif score ==75:
        print("u get 75")

elif score >= 60 or score >= 69:
    print("D")
else:
    print("F")



#learning about NESTED IS


