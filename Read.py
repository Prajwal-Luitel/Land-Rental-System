'''
This module is responsible for reading the file and displaying to user in appropirate
format.
'''

def fileToDic():
    """Read data from a file and store it into a dictionary."""
    dic = {} # Empty dictionary to store data
    key = 1 # Initialize key for dicitonary
    file = open("Land.txt","r") # Open file in reading mode
    #Iterate the line in file
    for line in file: 
        line = line.replace("\n","") # new line is replace by ,
        line = line.split(",")  # Split line into a list where data is sperated by ,
        dic[key] = line  # Assign the list to the dictionary 
        key = key + 1  # Increment key 
        
    file.close() # Close the file
    return dic 


def displayBilledFile(uniqueId):
    """
    Read the approprite rental file by distinguishing using unique id
    and Display it in shell
    """
    fileName = "rent_"+uniqueId + ".txt" # Open the file with uniqeId
    file = open(fileName,"r") # Open file in reading mode
    print(file.read()) # Display the entire file
    file.close() # Close the file


def displayReturendFile(uniqueId):
    """
    Read the approprite return file by distinguishing using unique id
    and Display it in shell
    """

    fileName = "Returned_"+uniqueId + ".txt" # Open the file with uniqeId
    file = open(fileName,"r") # Open file in reading mode
    print(file.read()) # Display the entire file
    file.close() # Close the file
