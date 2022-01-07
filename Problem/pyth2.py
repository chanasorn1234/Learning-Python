grade = []
subject = ["THAI","MATH","ENGLISH","SCIENCE","SPORT",]
i = 0
result = 0
while (i<5):
    x = float(input())
    grade.append(x)
    i += 1

for j in range(len(subject)):
    print(subject[j],"=",grade[j])

print("---")

for k in range(len(grade)):
    result += grade[k]
print("GPA =",result/5)
