
age=int(input("Enter your age"))
marriage= (input("Enter True if you are married else False"))
gender=str(input("Enter your gender(male/female)"))

if marriage == True :
    print("The driver is eligible for insuarance")
elif marriage == False:
    if gender == male:
        if age>30:
            print("The driver is eligible for insuarance")    
elif marriage == False:
    if gender == female :
        if age > 25:
            print("The driver is eligible for insuarance")
else:
    print("The driver is not eligible for insuarance")
