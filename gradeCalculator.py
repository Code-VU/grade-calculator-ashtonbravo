def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you

    score = input("Enter Score: ")
    try:
        s= float(score)
        if s<= 1.0:
            if s>=0.9 :
                print ('A')
            elif s>=0.8:
                print=("B")
            elif s>= 0.7:
                print=("C")
            elif s>=0.6:
                print=("D")
            elif s<= 0.6:
                print=("F")
        else:
            print= ("Bad score")
 
        

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateGrade() and run > python calculateGrade.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
## calculateGrade()