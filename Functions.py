# ----------------------------------------------------------------------------------------------------------------------------------
# Assignment Name:      Functions
# Name:                 Neina Cichon
# Date:                 2020-06-18
# ----------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------
# Function Name:      ValidateLoveMessage
# Function Purpose:   To validate all of the Love Message input
# ----------------------------------------------------------------------------------------------------------------------------------

def ValidateLoveMessage(String):  
    try:     
        if all(x.isalpha() or x.isspace() for x in String):
            global boolVal
            boolVal= True
            return strLoveMessage
        else:
            print("Please enter words only.")
    except ValueError:
        print("Please enter words only.")

    


# ----------------------------------------------------------------------------------------------------------------------------------
# Function Name:      ValidateInput
# Function Purpose:   To validate all of the input and make sure they are integers > 0
# ----------------------------------------------------------------------------------------------------------------------------------

def ValidateInput(input): 
    global boolFlag
    #boolFlag = False
    try:
        input = int(input)
        if (input > 0):
            boolFlag = True
        else:
            print("Don't be a negative Nancy. Please enter a positive integer.")
    except ValueError:
        input = int(0)
        print("You can't trick me! It must be a whole number.")
    return input



# ----------------------------------------------------------------------------------------------------------------------------------
# Function Name:     DisplayInstructions
# Function Purpose:  This displays the given message from the instructions  
# ----------------------------------------------------------------------------------------------------------------------------------

def DisplayInstructions( ):
    strMessage = ("""This program will demonstrate how to make and use procedures in Python...\nIn addition, it will demonstrate how to pass values and variables into a \nprocedure as parameters.  It will also demonstrate how Python deals with ByRef and ByVal.\n\n""")
    print(strMessage)



# ----------------------------------------------------------------------------------------------------------------------------------
# Function Name:      DisplayMessage
# Function Purpose:   To display the same message the number of times entered by the user 
# ----------------------------------------------------------------------------------------------------------------------------------

def DisplayMessage( strLoveMessage,intPrintCount ):
    intCount = int(0)
    while intCount < intPrintCount:
        print("I love", strLoveMessage,"!")
        intCount += 1



# ----------------------------------------------------------------------------------------------------------------------------------
# Function Name:    GetLargerValue  
# Function Purpose: Gets the larger number from the 2 given by the user    
# ----------------------------------------------------------------------------------------------------------------------------------

def GetLargerValue( intValue1, intValue2 ):
    print("\nThe larger number of ", intValue1, " and ", intValue2, " is ", max(intValue1, intValue2))



# ----------------------------------------------------------------------------------------------------------------------------------
# Function Name:      GetLargestValue
# Function Purpose:   Gets the largest value out of seven integers provided by user  
# ----------------------------------------------------------------------------------------------------------------------------------

def GetLargestValue( intValue1, intValue2, intValue3, intValue4, intValue5, intValue6, intValue7):
    numberList = [intValue1, intValue2, intValue3, intValue4, intValue5, intValue6, intValue7]
    print("\nThe largest number out of", intValue1, ", ", intValue2,", ",  intValue3,", ",  intValue4,", ",  intValue5,", ",  intValue6," and ",  intValue7, " is ", max(numberList))



# ----------------------------------------------------------------------------------------------------------------------------------
# Function Name:      CalculareSphereVolume
# Function Purpose:   Calculates the volume of the sphere based on the diameter given by the user  
# ----------------------------------------------------------------------------------------------------------------------------------

def CalculateSphereVolume(intDiameter):

    dblPi = float(3.1415926535897931)
    dblRadius = float(intDiameter/2)
    dblVolume = float()

    dblVolume = 4.0/3.0* dblPi * dblRadius**3
    print("The volume of a sphere with a ", intDiameter, " inch diameter = ", dblVolume )



# ----------------------------------------------------------------------------------------------------------------------------------
# Name:      Main Code
# Purpose:   Controlling Main Code for Applications           
# ----------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------
# Purpose: Call function to display the instructions             
# ----------------------------------------------------------------------------------------------------------------------------------

DisplayInstructions()



# ----------------------------------------------------------------------------------------------------------------------------------
# Purpose: Get user input for the message, and call function to display love message            
# ----------------------------------------------------------------------------------------------------------------------------------
strLoveMessage = str()
boolVal = bool(False)
boolFlag = bool(False)

while boolVal is False:
    strLoveMessage=str(input("What do you love? "))
    strLoveMessage = ValidateLoveMessage( strLoveMessage )

while boolFlag is False:
    
    intPrintCount = str(input("Enter number of times you want me to say it: "))
    intPrintCount = ValidateInput(intPrintCount)

DisplayMessage(strLoveMessage, intPrintCount)



# ----------------------------------------------------------------------------------------------------------------------------------
# Purpose: Get user input for two numbers, and Call the function to get the larger value         
# ----------------------------------------------------------------------------------------------------------------------------------

print("\n\nNow I will tell you the larger value between two numbers!")
boolFlag = False
while boolFlag is False:   
    intValue1 = str(input("Enter first number: "))
    intValue1 = ValidateInput(input = intValue1)
boolFlag = False
while boolFlag is False:
    intValue2 = str(input("Enter second number: "))
    intValue2 = ValidateInput(input = intValue2)

GetLargerValue(intValue1, intValue2)



# ----------------------------------------------------------------------------------------------------------------------------------
# Purpose: Get user input for seven numbers, and Call the function to get the largest value         
# ----------------------------------------------------------------------------------------------------------------------------------

print("\n\nThat was too easy...I can do better!\nI will tell you the largest value out of SEVEN numbers!!\n")
boolFlag = False
while boolFlag is False:   
    intValue1 = str(input("Enter first number: "))
    intValue1 = ValidateInput(intValue1)
boolFlag = False
while boolFlag is False:
    intValue2 = str(input("Enter second number: "))
    intValue2 = ValidateInput(intValue2)
boolFlag = False
while boolFlag is False:
    intValue3 = str(input("Enter third number: "))
    intValue3 = ValidateInput(intValue3)
boolFlag = False
while boolFlag is False:
    intValue4 = str(input("Enter fourth number: "))
    intValue4 = ValidateInput(intValue4)
boolFlag = False
while boolFlag is False:
    intValue5 = str(input("Enter fifth number: "))
    intValue5 = ValidateInput(intValue5)
boolFlag = False
while boolFlag is False:
    intValue6 = str(input("Enter sixth number: "))
    intValue6 = ValidateInput(intValue6)
boolFlag = False
while boolFlag is False:
    intValue7 = str(input("Enter seventh number: "))
    intValue7 = ValidateInput(intValue7)

GetLargestValue( intValue1, intValue2, intValue3, intValue4, intValue5, intValue6, intValue7)



# ----------------------------------------------------------------------------------------------------------------------------------
# Purpose: Get user input for sphere diameter, validate, and Call the function to get the volume of the sphere        
# ----------------------------------------------------------------------------------------------------------------------------------


print("\n\nI'm bored of that. Let's calculate something new!")
boolFlag = False
while boolFlag is False:
    intDiameter = str(input("\nEnter the diameter of the circle: "))
    intDiameter = ValidateInput(input = intDiameter)
CalculateSphereVolume(intDiameter)

print("\n\n\n-----------------------------------------------------\nThis program has been brought to you by Neina")

