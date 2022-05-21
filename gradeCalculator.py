#import sys

#def calculateGrade():
    # Implement your solution in between the two comment blocks
    #print("Calculating Grade")
    # This first line is provided for you


print('Calculating Grade')

#try: 
score = float(input('Enter Score: '))

if score > 1.0:
    print('Bad score')
elif 1.0 >= score >= .9:
    print('A' + str(score))
elif .9 > score >= .8:
    print('B')
elif .8 > score >= .7:
    print('C')
elif .7 > score >= .6:
    print ('D')
elif.6 > score >= .5:
    print('F')
else:
    print('Bad score')


    # end assignment


