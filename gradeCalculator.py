def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you

    score = input("Enter Score: ")
    score= float(score)
    x = 'Bad score'
    if s<= 1.0 and s>= 0.0:
        if s>=0.9:
            x=("A")
        elif s>= 0.8:
            x=("B")
        elif s>=0.7:
            x=("C")
        elif s>= 0.6:
            x=("D")
        elif s<0.6:
            x=("F")
        else:
            x= ("Bad score")
    print (x) 
        

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateGrade() and run > python calculateGrade.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
## calculateGrade()