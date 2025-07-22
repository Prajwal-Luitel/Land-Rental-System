'''
This module is responsible for writing the bill invoice to the file.
It also update the land status and add duration and customer to file.
'''
def rewriteTheFile(landId,dictionary):
    """
    Update the Land status whose landId matches in the dictionary key
    """
    file = open("Land.txt","w") # Open 'Land.txt' file in write mode
    # Iterate over the dictionary items
    for key,value in dictionary.items():
        if key == landId: #Only change status whose key matches with the ID
             # Update status to "Available"
            value[-3] = "Not Available"
        # Join the list elements with ',' and write to file    
        value = ",".join(value) 
        file.write(value+"\n") #New line after each list
    file.close() #Close the file


def fileGenerator(uniqueId,landId,listInfo,dictionary):
    """Write a bill in uniqueFile"""
    fileName = "rent_"+uniqueId + ".txt" #Unique file name
    file = open(fileName,"w") # Open  file in write mode
    # Iterate over the dictionary items 
    for key,value in dictionary.items():
        # Write the billing about the selected landId only"
        if key == landId:
            #Bill heading
            file.write("\n"+" "*25+"Land Billing\n")
            file.write(" "*55+"Phone No: 98425****\n")
            file.write(" "*20+"Techno propery Nepal pvt. ltd.\n")
            file.write(" "*25+"Kathmandu,Nepal\n")
            #User information
            file.write(" "*55+"Date: "+ listInfo[1] +"\n") # Date and time
            file.write(" "*60+"."*30+"\n")
            file.write("T0, " + listInfo[0]+"\n")# User name
            file.write(" "*3+"."*32+"\n\n")
            file.write("Customer Id: " + uniqueId+"\n")# Generated uniqeId
            # Desiging
            file.write(" "*12+"."*36+"\n\n")
            file.write("+"*70+"\n")
            # Rented land information
            file.write("\nKitta Number: "+value[0] + "\n") 
            file.write("Location: "+value[1] + "\n")
            file.write("Direction of Land: "+value[2] + "\n")
            file.write("Anna Details of Land: "+value[3] + "\n")
            file.write("Monthly Rate of Land: "+value[4] + "\n")
            file.write("Duration of Rent: "+str(listInfo[2]) + "\n")
            file.close() # Close the file
            break # Terminate when land id is found


def FurtherFileGenerator(uniqueId,landId,duration,dictionary):
    """Add further information in the exsting file"""
    fileName = "rent_"+uniqueId + ".txt" 
    file = open(fileName,"a") # Open the file in append mode
    # Iterate over the dictionary items  
    for key,value in dictionary.items():
        # Write the billing about the selected landId only"
        if key == landId:
           # Further rented land information
           file.write("\nKitta Number: "+value[0] + "\n")
           file.write("Location: "+value[1] + "\n")
           file.write("Direction of Land: "+ str(value[2]) + "\n")
           file.write("Anna Details of Land: "+value[3] + "\n")
           file.write("Monthly Rate of Land: "+value[4] + "\n")
           file.write("Duration of Rent: "+ str(duration) + "\n")
           file.close() # Close the file
           break # Terminate when id is found

            
def totalPriceInFile(uniqueId,total):
    """This function write total price over an existing file"""
    fileName = "rent_"+uniqueId + ".txt"
    file = open(fileName,"a") # Open the file in append mode
    # Write the total price in unique file
    file.write("\n"+"*"*80+"\n")
    file.write(" "*57+"Grand Total: "+str(total) + "\n")
    file.close() # Close the file


def  returnedBillingFile(landId,uniqueId,returnedTime,dictionary):
    """This function write invoice the returned land """
    fileName = "returned_"+uniqueId + ".txt"
    '''
    The file is opened in append mode instead of write mode because writing override from the existing
    file while append write in it. It is made so that user can return multiple land at different time and the
    data is writed in file instead of overwriting the new data
  
    '''
    file = open(fileName,"a")
    # Iterate over the dictionary items 
    for key,value in dictionary.items():
        # Write the invoice about the selected landId only"
        if key == landId:
            # Bill heading
            file.write("\n"+" "*25+"Land Invoice\n")
            file.write(" "*55+"Phone No: 98425****\n")
            file.write(" "*20+"Techno propery Nepal pvt. ltd.\n")
            file.write(" "*25+"Kathmandu,Nepal\n\n")
            # User information
            file.write("T0, " +  uniqueId[:-8]+"\n") #Only showing User name from unique Id
            file.write(" "*3+"."*32+"\n\n")
            file.write("Customer Id: " + uniqueId+"\n") #UniqueId
            file.write(" "*12+"."*36+"\n\n")
            #Returned land Information
            file.write("+"*80+"\n\n")
            file.write("\nKitta Number: "+value[0] + "\n")
            file.write("Location: "+value[1] + "\n")
            file.write("Direction of Land: "+value[2] + "\n")
            file.write("Anna Details of Land: "+value[3] + "\n")
            file.write("Monthly Rate of Land: "+value[4] + "\n\n")
            file.write("Estimated Returned Duration : "+str(value[-2]) + "\n")
            file.write("Actual Returned Duration : "+str(returnedTime) + "\n")
            file.close()# Close the file
            break    # Terminate when land id is found


def returnFurtherFileGenerator(uniqueId,landId,returnedTime,dictionary):
    """This funciton generated the information about further landId that is returned"""
    fileName = "returned_"+uniqueId + ".txt"
    file = open(fileName,"a") # Open the file in append mode
    # Iterate over the dictionary items 
    for key,value in dictionary.items():
        # Write the land information the selected landId only"
         if key == landId:
             # Land information
             file.write("\nKitta Number: "+value[0] + "\n")
             file.write("Location: "+value[1] + "\n")
             file.write("Direction of Land: "+value[2] + "\n")
             file.write("Monthly Rate of Land: "+value[4] + "\n\n")
             file.write("Estimated Returned Duration : "+str(value[-2]) + "\n")
             file.write("Actual Returned Duration : "+str(returnedTime) + "\n")
             file.close()# Close the file
             break # Terminate when land id is found


def returnTotalPriceInFile(uniqueId,price,charge):
    """Write the price and charge and total amount in the invoice"""
    total = price+charge
    fileName = "returned_"+uniqueId + ".txt" 
    file = open(fileName,"a") # Open the file in append mode
    # Writing the pricing in returned unique file
    file.write("\n"+"*"*83+"\n")
    file.write(" "*52+"Actual Price: "+str(price) + "\n")
    file.write(" "*52+"Charge Amount: "+str(charge) + "\n")
    file.write(" "*52+"Total Amount: "+str(total) + "\n")  
    file.close()# Close the file

    
def ReturnedrewriteTheFile(landId,dic):
    """Change the land status from Not Available to Available of the given land Id
       Make the change in file from the data store in dictionary
    """
    file = open("Land.txt","w") # Open the file in writing mode
    # Iterate over the dictionary items
    for key,value in dic.items():
        if key == landId: # Found the given land Id
            # Make the changes
            value[-3] = "Available"
            value[-2] = "duration"
            value[-1] = "UniqueId"
        value = ",".join(value) #Join the list element with ,
        file.write(value+"\n") #New lilne
    file.close()#Close the file
            
