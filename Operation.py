'''
All the logical operation reqired to run the program is carried here.
'''
import datetime #Importing datetime to read the current time
# Importing all the function from Read and Write module
from Read import *
from Write import *


def chooseOption():
    """ Option the user have  """
    #Exception handling
    while  True:
        print("\n\nEnter '1' to rent land")
        print("Enter '2' to return land")
        print("Enter '3' to exit")
        
        try:

            number = int(input("Please enter a value: "))
            print("")
            return number
        except:
           print("\nPlease enter numeric value")


def displayFile(dictionary):
    """Display the dictionary data in tabular format"""
    
    print("\n\n\n"+"-"*115) #print - 115 times
    print("Land ID    Kitta No       City/Distict Name     Direction        Anna             Price        Avaliability Status ")
    print("-"*115)
    # Iterate over dictonary items
    for key,value in dictionary.items():
        #Format the table with f-string 
        print("  ",f"{key:<10}",end = " ") # To make the landId space 10 for any digit of id
        for item in value:
            if item == value[-2] or item == value[-1]:
               print("",end = " ")#Skip the last two value of list in dictionary
            else:
               print(f"{item:<16}",end = " ")#Make the space along with item to be 16 regardless of its size 
        print()
        
    print("-"*115+"\n\n") #print - 115 times


   
def giveOutput(userChoice):
    """ Give the message to the user selected functionality and also give landId if user select"""
    # Exception handling
    while True:
        try:
            if userChoice == 1:
                option = int(input("Enter the ID of Land you want to borrow: "))
                return option, 1 #Returning land Id and message to user choice
            #returning message to user choice
            elif userChoice == 2:
                print("You will now return the land")
                return None, 2 
            
            elif userChoice == 3:
                print("Thanks for using our land management system.")
                return None, 3
            
            else:
                print("+" * 56)
                print("Invalid input!!!")
                print("Please provide value as 1, 2 or 3.")
                print("+" * 56)
                return None, 4
        except:
            print("\nPlease enter numeric value\n")

def landAvaliability(landId,dictionary):
    """This fuction check the land status and also check the valid land and give appropriate message"""
    # Checking if land is valid or not
    if landId > 0 and landId <= len(dictionary):
        # Iterating over dictonary items
        for key,value in dictionary.items():
            #When Id mataches
            if key == landId: 
                print("\n Land ID is",landId)
                print()
                #Checking land status
                if value[-3] == "Available":
                    print("+"*56)
                    print(" "*9+"Land is available!!!")
                    print("+"*56)
                    return 1
                
                else:
                    print("+"*56)
                    print(" "*9+"Land is  not available!!!")
                    print("+"*56)
                    displayFile(dictionary) #Displaying the file in tabular format
                    return 2
                        
    else:
        print()
        print("+"*56)
        print(" "*9+"Please provide a valid Land ID!!!")
        print("+"*56)
        displayFile(dictionary)
        return  3


def userInfo():
    """This funtion take the user information and user wish to rent more or not"""
    name = input("\nEnter the name of person who borrowed land: ")
    time = str(datetime.datetime.now()) 
    print("Date and Time of borrow is :",time[:22]) #Displaying the date and time upto 22 value
    # Exception handling
    while True:
        try:
            #Only taking the valid duraton
            validDuration = False
            
            while validDuration == False:
                duration = int(input("Enter the number of month for which the land is rented: "))
                if duration < 0:
                    print("\nDuration cannot be negative \n")
                elif duration == 0:
                    print("\nDuration cannot be zero \n")
                elif duration >= 36:
                    print("\nSorry you cannot rent the land more than 36 months\n")
                else:
                    validDuration = True
            #Terminating the lopp when valid duration is found      
            if validDuration == True:
                break
            
        except:
            print("\nDuration cannot be alphabet \nPlease Enter  valid numric value\n")
    print("\n"+"="*65+"\n")
    print("Do you want to rent another land")
    #User continuation  
    wish = input("Provide 'n' if you do not want to rent another land else provide any other value: ")
    if wish == "n":
        wish = False
    else:
        wish = True
        
    return name,time,duration,wish


def userInfoContinuation(dictionary):
    """
       Take the information of the land if user want to continue and if invalid id is given then again ask
       the user to contiue or exit
    """
    invalidExit = 0
    displayFile(dictionary) # Display the data in tabular format
    
    while True:
        landId = giveOutput(1) # Taking the land Id from user
        Avaliability = landAvaliability(landId[0],dictionary)  #   Checking the land Id is valid or not     
        if Avaliability == 1:
           # Exception handling  
            while True:
                try:
                    validDuration = False
                    while validDuration == False:
                        duration = int(input("Enter the number of month for which the land is rented: "))
                        if duration < 0:
                            print("\nDuration cannot be negative \n")
                        elif duration == 0:
                            print("\nDuration cannot be zero \n")
                        elif duration >= 36:
                            print("\nSorry you cannot rent the land more than 36 months\n")
                        else:
                            validDuration = True
                            
                    if validDuration == True:
                        break
                    
                except:
                    print("\nDuration cannot be alphabet \nPlease Enter  valid numric value\n")
            # User want to continue or not
            wish = input("\nProvide 'n' if you do not want to rent another land else provide any other value: ")   
            if wish == "n":
                wish =  False
            else:
                wish =  True
            return landId[0],duration,wish,invalidExit
            
        else:
            #When land id is invalid and user want to exit
            print()
            wish = input("Provide 'n' if you do not want to rent another land else provide any other value: ")
              
            if wish == "n":
                invalidExit = 1
                return wish,invalidExit


def bill(duration,landId,dic):
    """Calculate the total price of land"""
    rate = 0
    #Check for the user landId in dictionary
    for key,value in dic.items():
        if key == landId:
           rate = int(value[4])
           break
        
    fee = int(duration) * rate
    return fee


def uniqueId(name):
    """
       This function take name and genrate random number to make the name unique
       It uses date and time to generate random number
    """
    minute = str(datetime.datetime.now().minute) #Taking minute
    second = str(datetime.datetime.now().second) #Taking second
    microsecond = str(datetime.datetime.now().microsecond)[:2] #Taking microsecond only upto 2 digit 
    uniqueValue = minute + second + microsecond
    return name + "("+uniqueValue+")"


def addUniqueIdInDictionary(landId,uniqueId,duration,dictionary):
    """It store the uniqueId and duration of land of user in dictionary"""
    for key,value in dictionary.items():
        if key == landId:
            value[-2] = str(duration)
            value[-1] = uniqueId
            break #Terminate when the landId is found


def returnLandDisplay(dictionary, customerId):
    """Display the tabluar format of only the land user has rented"""
    #Make table
    print("\n\n"+"-"*126)
    print("Land ID    Kitta No       City/Distict Name     Direction        Anna             Price      Avaliability Status   Duration")
    print("-"*126)
    # Iterating over dicionary
    for key, value in dictionary.items():
        #Checking the land user has rented
        if value[-1] == customerId:
            print("  ", f"{key:<10}", end=" ") # To make the landId space 10 for any digit of id
            for item in value:
                if item == value[-1]: 
                    print("",end = " ") #Skip the last list value of dictionary
                else:
                    print(f"{item:<16}", end=" ") #Make the spacing only  16 with word regard less of the word 
            print()
    print("-"*126)
      
    
def returnLandCondiition(landId,dictonary,customerId):
    """Checking if the user provide valid land Id or not"""
    validLandId = 0
    #Itetrating over dictionary
    for key,value in dictonary.items():
          if landId == key:
             matchCustomerId = 1
             validLandId = 1

             if value[-1] == customerId:
                if value[-3] != "Available": 
                    print(" ")
                    return 1
             print("The user has not rented this Land")
             return 2
    #LandId not in dictionary        
    if validLandId == 0:
        print("\n"+"+"*56)
        print("         Please provide a valid Land ID!!!")
        print("+"*56)
        return  3

        
def returnReturnedBill(landId,returnedDuration,dictionary):
    """Calculating the total price user should pay along with fee if late returned"""
    charge = 0
    for key,value in dictionary.items():
        if key == landId: 
           #When user return in time
           if int(returnedDuration) <= int(value[-2]): # value[-2] is duration
               price = int(value[-2]) * int(value[4]) # value[4] is rate
               return price, charge
           #When user failed to return in time
           else : 
               price = returnedDuration * int(value[4])
               extraDuration = returnedDuration - int(value[-2]) # value[-2] is duration
               charge = 0.10 * (extraDuration * int(value[4]) ) # value[-2] is duration
               return  price, charge


def rentLand(landId,dictionary):
        """rentLand is a function that call all  land data is given and user has to pick
           landId with duration. For renting the land when ever the user click invalid land
           land  the program ask to continue or not and when user say  no the program return
            to main menu and bill is printed if user has inputed landid and duration. User can
            rent one and multiple rent at a time
           
       """
        total = 0 #Price of all land
        while True: 
            Avaliablility = landAvaliability(landId, dictionary) #Check if the user inputed land is valid or not
            #The while work only when valid landId is given
            while Avaliablility == 1:
                userList = userInfo() #Collect user information about the land
                #From tuple to variable
                name = userList[0]
                duration = userList[2]
                uniqueID = uniqueId(name)
                wish = userList[3]
                #Add the uniqueId along with duration in dictionary
                addUniqueIdInDictionary(landId,uniqueID,duration,dictionary) # Add the duration and uniqueId in dictionary
                fileGenerator(uniqueID, landId, userList, dictionary) # Generate billing file
                total += bill(duration, landId, dictionary) # price is added to total
                ''' The land status is changed to Not avaiable and readded UniqueId,
                     duration to dictionary is added to file'''
                rewriteTheFile(landId, dictionary) 
                if wish == False: # User want to stop renting
                    totalPriceInFile(uniqueID,total) # Add price in file 
                    displayBilledFile(uniqueID) # Display the file in shell
                    return # terminate the function
                
                while wish: # User want to rent more land
                    userInfoContinuationTuple = userInfoContinuation(dictionary) #Further land information is added in tuple
                    #From tuple to variable
                    invalidExit = userInfoContinuationTuple[-1]
                    wish = userInfoContinuationTuple[-2]
                    landId = userInfoContinuationTuple[0]
                    duration = userInfoContinuationTuple[1]
                    # User want to stop renting
                    if invalidExit == 1:
                       totalPriceInFile(uniqueID,total) # Add price in file 
                       displayBilledFile(uniqueID) # Display the file in shell
                       return # terminate the function
                    #User want to rent more 
                    addUniqueIdInDictionary(landId,uniqueID,duration,dictionary) #  Add the duration and uniqueId in dictionary
                    FurtherFileGenerator(uniqueID, landId, duration, dictionary) # Generate the further rented land details in file
                    total += bill(duration, landId, dictionary) # Add the price in total
                    '''
                       The land status is changed to Not Avaiable and readded UniqueId,
                       duration to dictionary is added to file
                    '''
                    rewriteTheFile(landId, dictionary) 
                    #User want to stop renting
                    if wish == False:
                        totalPriceInFile(uniqueID,total) # Add total price in file
                        displayBilledFile(uniqueID) # Display the file
                        return
            #When invalid Id is given       
            if Avaliablility == 3 or Avaliablility == 2:
                wish = input("Do you wish to continue if no press n else press any: ")
                if wish == "n": 
                    return # Terminate the function
                LandIdTupele = giveOutput(1) # Again take LandId
                landId = LandIdTupele[0] # inputted landId is stored
                

                
def returnLand(dictionary):
    """ rerutnLand function is resposible for returing the land it take customerId and matches it
        give customer rented land user input the land and if it is valid land then returned duration
        is asked and invoice is generated  with price and charge if late return user can rent multiple
        rent at once and when ever wrong land id customer id is given the software ask for continuation
        and when user want to exit to return to main menu
    """ 
    while True:
        customerId = input("Enter your customer Id (eg:- name(123456)): ")
        price = 0
        charge = 0
        customer = 0 #Chcek for valid customerId
        for key,value in dictionary.items():
            if value[-1] == customerId:     #The customerId is vaild
                while True:
                    customer = 1
                    returnLandDisplay(dictionary, customerId)
                    # Exception handling
                    while True:
                        try:
                            landId = int(input("Enter the ID of the land you want to return: "))
                            break
                        except:
                            print("\nPlease Enter numeric value\n")
                    # Checking for valid landId        
                    condition = returnLandCondiition(landId,dictionary,customerId) 
                    # Valid Id is found
                    while condition == 1:    
                        # Exception handling
                        while True:
                            try:
                                validDuration = False # Checking for valid Duration along with Execption
                                while validDuration == False:
                                    reuturnedDuration = int(input("Enter the number of month for which the land is kept: "))
                                    if reuturnedDuration < 0:
                                        print("\nDuration cannot be negative \n")
                                    elif reuturnedDuration == 0:
                                        print("\nDuration cannot be zero \n")
                                    else:
                                        validDuration = True
                                        
                                if validDuration == True:
                                    break
                            except:
                                print("\nDuration cannot be alphabet \nPlease Enter  valid numric value\n")
                        # User is ask to continuing returning       
                        wish = input("Do you wish to continue if no press n else press any:")
                        returnedBillingFile(landId,customerId,reuturnedDuration,dictionary) # Write invoice in file
                        # price along with charge is returned in tuple
                        returnedPriceTuple = returnReturnedBill(landId,reuturnedDuration,dictionary)
                        price += returnedPriceTuple[0] # Price is added 
                        charge += returnedPriceTuple[1] # Charge is added
                        # Land status is set to Availabe and duration and userId is removed
                        ReturnedrewriteTheFile(landId,dictionary) 
                        # if user want to stop returning
                        if wish == "n":
                            # write total price  along with price and charge in file
                            returnTotalPriceInFile(customerId,returnedPriceTuple[0],returnedPriceTuple[1]) 
                            displayReturendFile(customerId) # Display the file in shell
                            return # Terminate the function
                        # User want to return more
                        while True:    
                            returnLandDisplay(dictionary, customerId)
                            # Exception handling
                            while True:
                                try:
                                    landId = int(input("Enter the ID of the land you want to return: "))
                                    break
                                except:
                                    print("\nPlease Enter numeric value\n")
                            # Checking for valid landId 
                            condition = returnLandCondiition(landId,dictionary,customerId)
                            # Valid Id is found
                            while condition == 1:
                                # Exception handling
                                while True:
                                    try:
                                        validDuration = False
                                        while validDuration == False:
                                            reuturnedDuration = int(input("Enter the number of month for which the land is kept: "))
                                            if reuturnedDuration < 0:
                                                print("\nDuration cannot be negative \n")
                                            elif reuturnedDuration == 0:
                                                print("\nDuration cannot be zero \n")
                                            else:
                                                validDuration = True
                                                
                                        if validDuration == True:
                                            break
                                    except:
                                        print("\nDuration cannot be alphabet \nPlease Enter  valid numric value\n")
            
                                wish = input("Do you wish to continue if no press n else press any:")
                                # Add further returned information in same file
                                returnFurtherFileGenerator(customerId,landId,reuturnedDuration,dictionary)
                                # price along with charge is returned in tuple
                                returnedPriceTuple = returnReturnedBill(landId,reuturnedDuration,dictionary)  
                                price += returnedPriceTuple[0] # Price is added
                                charge += returnedPriceTuple[1] # Price is added
                                # Land status is set to Availabe and duration and userId is removed
                                ReturnedrewriteTheFile(landId,dictionary) 
                                if wish == "n":
                                    # write total price  along with price and chargein file
                                    returnTotalPriceInFile(customerId,price,charge) 
                                    displayReturendFile(customerId) # Display the returned invoice in shell
                                    return
                                else:
                                    break
                            # User input invalid landId   
                            if condition == 2 or condition == 3:
                                wish = input("Do you wish to continue if no press n else press any: ")
                                if wish == "n":
                                    returnTotalPriceInFile(customerId,price,charge)
                                    displayReturendFile(customerId)
                                    return
                    # User input invalid landId               
                    if condition == 2 or condition == 3:
                        wish = input("Do you wish to continue if no press n else press any: ")
                        if wish == "n":
                            return
        #The customer Id is invalid                    
        if customer == 0:    
            print("Invalid customer Id")
            wish = input("Do you wish to continue if no press n else press any: ")
            if wish == "n":
                break
