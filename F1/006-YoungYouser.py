age = int(input("Please enter your age: "))
if 0 < age < 6:
    print("Khordsal")
elif 6 < age < 10:
    print("Koodak")
elif 10 <= age < 14:
    print("Nojavan")
elif 14 <= age < 24:
    print("Javan")
elif 24 <= age < 40:
    print("Bozorgsal")
elif age >= 40:
    print("Miansal")
else:
    print("Invalid age")