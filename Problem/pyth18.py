score = int(input())
if(score >= 90):
    print("A")
elif(score >= 85 and score < 90):
    print("B+")
elif(score >= 80 and score < 85):
    print("B")
elif(score >= 75 and score < 80):
    print("C+")
elif(score >= 70 and score < 75):
    print("C")
elif(score >= 65 and score < 70):
    print("D+")
elif(score >= 60 and score < 65):
    print("D")
else:
    print("F")