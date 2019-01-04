#varibles
q1C = False

#intro
print("you will answer this multiple chocie question answer question 1-4 only")

while q1C == False:
    try:
        l = int(input("What is 2+2"))
        print("1: 4")
        print("2: 3")
        print("3: 1")
        print("4: 5")
        if 0 < int < 5:
            q1C = True
        else:
            print("good job answering")
