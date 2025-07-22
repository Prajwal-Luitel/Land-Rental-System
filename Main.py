'''
This module is resposible for running the code.
'''
# Importing all the function from Opeation,Message and Read module
from Operation import *
from Message import *
from Read import *

def main():
    """It is the main function that execute the program by calling other function"""
    welcome() # Call the fuction that displaying welcome message
    dictionary = fileToDic() # Call the function that store file data in dictionary
    #The loop run infinitely unless user chooses to exit
    while True: 
        displayFile(dictionary) # Call the fuction that dispaly dictionary data in tabular fomat
        optionNumber = chooseOption() # store the functionality that user want
        landIdOrCondition = giveOutput(optionNumber) #Give the message to the user selected functionality and also give landId if user select
        #Store the data of tuple in variable
        landId = landIdOrCondition[0] 
        condition = landIdOrCondition[1]
        
        if condition == 1: # RentLand fuction is call when user choose to rent the land
            rentLand(landId,dictionary) 
               
        elif condition == 2: # returnLand fuction is call when user want to return the land
            returnLand(dictionary)
            
        elif condition == 3: # The program terminate 
            break
            

main() # call the main function
