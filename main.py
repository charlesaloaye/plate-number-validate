#A Plate Number Validator


def plate_number_validator(plate_number):

    '''
    This program will validate plate number
    '''

        #making sure plate number has 6 or 7 input are letters
    if (len(plate_number) == 6 or len(plate_number) == 7):
        
        #making sure plate number first 3 input are letters and capital letters
        if plate_number[0:3].isalpha and plate_number[0:3].upper() and plate_number[0:3]:
            #print('Valid plate number')    
            print(plate_number, 'is a new plate number')

        #making sure plate number first 2 input are letters and capital letters
        elif plate_number[0:2].isalpha and plate_number[0:2].upper() and plate_number[0:2]:
            print(plate_number, 'is an old plate number')    

        else:
            print(plate_number, 'is not a plate number')    

    else:
         print('invalid plate number')    

plateNumber = input("Enter plate number\n")
plate_number_validator(plateNumber)
