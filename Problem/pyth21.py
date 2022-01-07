w = int(input())
h = int(input())

BMI = w/pow((h/100),2)  
print("%.2f"%BMI)
if(BMI < 18):
    print("Thin")
if(BMI>=18 and BMI <= 22):
    print("Good Health")
if(BMI>=23 and BMI <= 24):
    print("Fat Level 1")
if(BMI>=25 and BMI <= 29):
    print("Fat Level 2")
if(BMI>=30):
    print("Fat Level 3")