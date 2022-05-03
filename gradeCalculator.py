def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you
Print('Calculating Grade')

try: 
    score = float(input('Enter Score: '))

    if score > 1:
        print('Bad score')
    elif score >= 0.9:
        print('A')
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score>= 0.6:
        print ('D')
    elif score >= 0:
        print('F')
    else:
        print('Bad score')
except:
    print('Bad score')


    # end assignment


