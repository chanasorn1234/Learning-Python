floor = input()
if(int(floor) >= 1 and int(floor) <= 5):
    print("OK! Wait please")
    print("---------------")
    print("Lift is arriving!")
    print("---------------")
    print("Lift is going up!")
    print("---------------")
    if(floor == "1"):
        print("Lift has reached the 1st floor!")
    elif(floor == "2"):
        print("Lift has reached the 2nd floor!")
    elif(floor == "3"):
        print("Lift has reached the 3rd floor!")
    else:
        print("Lift has reached the",str(floor)+"th floor!")
else:
    print("Error! Not have this floor")