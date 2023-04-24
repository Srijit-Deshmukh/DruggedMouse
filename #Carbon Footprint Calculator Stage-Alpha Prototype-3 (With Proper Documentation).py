#Carbon Footprint Calculator for Individuals {Montly/Anually}

import streamlit 
streamlit.write('''
#Hello World!
''')
#User Freindly
#In-built safety features
#Instant Results with Comparision
#Personalised Recommendations to the User
#Lite and fast
#Easy to Debug
#Complete Documentation Included

"""Carbon Emission Factors:                                                  
01.Electricity = 0.08                        
02.Coal = 2500                          
03.Coke = 2800
04.Wood = 700
05.LPG = 2.98
06.Air Travel = 0.32 (International)
   Air Travel = 0.16 (Domestical)
07.Train Travel = 0.06
08.Bus Travel = 0.09
09.Car Travel (Petrol) = 2.3
   Car Travel (Diesel) = 2.6"""

#A Function that Terminates the Program instantly when an invalid numeric value is taken as an input.
def Logic_Check(A):
    if A < 0:
        print()
        print("""Unexpected Error from the User End!
        Try Again!""")
        exit()

#A Function that Terminates the Program instantly when the user gives anything else other than the intended inputs.
def User_Is_BrainDed():
    print()
    print("""Unexpected Error from the User End!
    Try Again""")
    exit ()

#A Function that round off the numeric values upto 3 decimal places
def Round_off(a,b,c):
    c = round(a,b)
    return c

#Coverts the values from Kilograms to Metric Tonnes 
def Kilogram_To_Tonnes(a):
    global c
    c = a/1000
    return c

#This section asks the user their time period for which they want to Calculate their Carbon Footprint
Time_Period = input("Enter Your Time Period for Calculation (Monthly/Yearly):")

#Steps taken to Make the Code More User Friendly and to overlook minor mistakes
Time_Period = Time_Period.strip()
Time_Period = Time_Period.lower()

#Evaluation
if Time_Period == "monthly":
    T = "Monthly"
elif Time_Period == "yearly":
    T = "Yearly"
else :
    User_Is_BrainDed()       #Safety Measure Function Call

#This section asks the user about the no. of ppl they live with 
#This information is important because the CO2e Emissions in a household is shared by all the individuals equally 
Family_Members = int(input("How many People does live in your Household:"))
#Evaluation
if Family_Members > 1 :       
    Live_Alone = False                                                           
elif Family_Members == 1:
    Live_Alone = True
else:
    User_Is_BrainDed()        #Safety Measure Function Call

print()   #This print() statement is written for the sake of making the terminal not look chaotic

#Section 01_C02e Due to Fuel Consumption :-

#Carbon Footprint Caused by Electricity Usage

ELECTRICITY_CarbonFootprint = 0  #Pre-defining Variables
Electricity_Use = 0              #Pre-defining Variables

Electricity_Usage = float(input(f"Enter Your Electricity Usage {T} (KwH):"))
#One Should Easily Access This Info Through Their Electricity Bills
Logic_Check(Electricity_Usage)   #Safety Measure Function Call
#Evaluation
if Electricity_Usage == 0:
    Electricity_Use = False                                                                     #Suggestion_Point_01
else:                                                                
    ELECTRICITY_CarbonFootprint = (Electricity_Usage)*0.82                                      #Final_Variable_01

print()    #This print() statement is written for the sake of making the terminal not look chaotic

#This parameter determines whether the user uses coal as a source of fuel.

COAL_CarbonFootprint = 0    #Pre-defining Variables
Coal_Use = 0                #Pre-defining Variables
Fuel_Usage_Coal = input("Do You Use Coal as a Source of Fuel (Yes/No):")
#Steps taken to Make the Code More User Friendly and to overlook minor mistakes
Fuel_Usage_Coal = Fuel_Usage_Coal.strip()
Fuel_Usage_Coal = Fuel_Usage_Coal.lower()
#Evaluation
if Fuel_Usage_Coal== "yes":
    COAL_CarbonFootprint = float(input(f"How much Coal(Tonnes) Do You use as Fuel {T}:"))   
    Logic_Check(COAL_CarbonFootprint)
    COAL_CarbonFootprint = COAL_CarbonFootprint * 2500                                      #Final_Variable_02
    Coal_Use = True                                                                         #Suggestions_Point_02
elif Fuel_Usage_Coal == "no":
    Coal_Use = False
else:
    User_Is_BrainDed()    #Safety Measure Function Call

print()   #This print() statement is written for the sake of making the terminal not look chaotic

#This parameter determines whether the user uses coke as a source of fuel.

COKE_CarbonFootprint = 0    #Pre-defining Variables
Coke_Use = 0                #Pre-defining Variables
Fuel_Usage_Coke = input("Do You Use Coke as a Source of Fuel (Yes/No):")
#Steps taken to Make the Code More User Friendly and to overlook minor mistakes
Fuel_Usage_Coke = Fuel_Usage_Coke.strip()
Fuel_Usage_Coke = Fuel_Usage_Coke.lower()
#Evaluation
if Fuel_Usage_Coke == "yes":
    COKE_CarbonFootprint = float(input(f"How much Coke (Tonnes) Do You use as Fuel {T}:"))   
    Logic_Check(COKE_CarbonFootprint)
    COKE_CarbonFootprint = COKE_CarbonFootprint*2800                                        #Final_Variable_03
    Coke_Use = True                                                                         #Suggestions_Point_03
elif Fuel_Usage_Coke == "no":
    Coke_Use = False
else:
    User_Is_BrainDed()      #Safety Measure Function Call

print()       #This print() statement is written for the sake of making the terminal not look chaotic

#This parameter determines whether the user uses Wood as a source of fuel.

WOOD_CarbonFootprint = 0   #Pre-defining Variables
Wood_Use = 0               #Pre-defining Variables
Fuel_Usage_Wood = input("Do You Use Wood as a Source of Fuel (Yes/No):")
#Steps taken to Make the Code More User Friendly and to overlook minor mistakes
Fuel_Usage_Wood = Fuel_Usage_Wood.strip()
Fuel_Usage_Wood = Fuel_Usage_Wood.lower()
#Evaluation
if Fuel_Usage_Wood == "yes":
    WOOD_CarbonFootprint = float(input(f"How much Wood (Tonnes) Do You use as Fuel {T}:"))   
    Logic_Check(WOOD_CarbonFootprint)
    WOOD_CarbonFootprint = WOOD_CarbonFootprint*700                                         #Final_Variable_04
    Wood_Use = True                                                                         #Suggestions_Point_04
elif Fuel_Usage_Wood == "no":
    Wood_Use = False
else:
    User_Is_BrainDed()       #Safety Measure Function Call      

print()      #This print() statement is written for the sake of making the terminal not look chaotic

#This parameter determines whether the user uses LPG as a source of fuel. 

LPG_CarbonFootprint = 0   #Pre-defining Variables
Lpg_Use = 0               #Pre-defining Variables
Fuel_Usage_LPG = input("Do You Use LPG as a Source of Fuel (Yes/No):")
#Steps taken to Make the Code More User Friendly and to overlook minor mistakes
Fuel_Usage_LPG = Fuel_Usage_LPG.strip()
Fuel_Usage_LPG = Fuel_Usage_LPG.lower()
#Evaluation
if Fuel_Usage_LPG == "yes":
    Cylinder_BIG = float(input(f"How many Large-sized LPG Cylinders Do you Use {T}:"))      #14.2 Kg
    Cylinder_Medium = float(input(f"How many Medium-sized LPG Cylinders Do you Use {T}:"))  #5 Kg
    Cylinder_Smol = float(input(f"How many Small-Sized LPG Cylinders Do you use {T}:"))     #2 Kg
    LPG_CarbonFootprint=((Cylinder_BIG*14.2)+(Cylinder_Medium*5)+(Cylinder_Smol*2))       
    Logic_Check(LPG_CarbonFootprint)
    LPG_CarbonFootprint = LPG_CarbonFootprint*2.98                                        #Final_Variable_05
    Lpg_Use = True                                                                        #Suggestion_Point_05
elif Fuel_Usage_LPG == "no":
    Lpg_Use = False
else:
    User_Is_BrainDed()        #Safety Measure Function Call   

print()         #This print() statement is written for the sake of making the terminal not look chaotic

#Generation of Results  for Fuel Consumption
Total_CarbonFooprint_FuelConsumption=ELECTRICITY_CarbonFootprint+COAL_CarbonFootprint+COKE_CarbonFootprint+WOOD_CarbonFootprint+LPG_CarbonFootprint
Family_CarbonFootprint_FuelCinsumption = Total_CarbonFooprint_FuelConsumption/Family_Members
Round_off(Total_CarbonFooprint_FuelConsumption,3,Total_CarbonFooprint_FuelConsumption)
Round_off(Family_CarbonFootprint_FuelCinsumption,3,Family_CarbonFootprint_FuelCinsumption)

#Section 01_C02e Due to Transportation :-

#The Section of the Code deals with the Carbon Emission due to the users usage of Plane as a mode of transport
Plane_Domestic_CarbonFootprint = 0       #Pre-defining Variables
Plane_International_CarbonFootprint = 0  #Pre-defining Variables
Plane_Use_Excess = 0                     #Pre-defining Variables
Plane_Use = 0                            #Pre-defining Variables
Plane = input(f"Have you taken any flights this {T[0:-2]} (Yes/No):")
#Steps taken to Make the Code More User Friendly and to overlook minor mistakes
Plane = Plane.strip()
Plane = Plane.lower()
#Evaluation
if Plane == "yes":
    Plane_Domestic=int(input("How many of those flights were domestical:"))
    Distance = float(input("Enter The Distance Travelled(Km):"))
    Logic_Check(Plane_Domestic)
    Logic_Check(Distance)
    #This section of the code determines whether the User is Using Aviation mode of Transport Excessively or not
    if Plane_Domestic > 0 :
        Plane_Domestic_CarbonFootprint = Plane_Domestic*Distance
        if Plane_Domestic >= 2:
            Plane_Use_Excess = True                                                         #Suggestion_Point_06
        else:
            Plane_Use_Excess = False

    print()      #This print() statement is written for the sake of making the terminal not look chaotic

    Plane_International=int(input("How many of those flights were International:"))
    Distance = float(input("Enter The Distance Travelled(km):"))
    #Safety Measure Function Call   
    Logic_Check(Plane_International)
    Logic_Check(Distance)
    if Plane_International >= 0: 
        Plane_International_CarbonFootprint = Plane_International*Distance
    Plane_Use = True
elif Plane == "no":
    Plane_Use = False                                                                        #Suggestion_Point_07
else:
    User_Is_BrainDed()               #Safety Measure Function Call   

print()         #This print() statement is written for the sake of making the terminal not look chaotic

PLANE_CarbonFootprint=Plane_International_CarbonFootprint+Plane_Domestic_CarbonFootprint      #Final_Variable_06

#Exception Case for User is Trolling

if PLANE_CarbonFootprint == 0 and Plane_Use == True:
    print("Why did you say yes if you have not travelled by any flights this year!")
    Plane_Use = False
else:
    Plane_Use = True
print()

#This parameter determines whether the user uses Railway Lines as a mean of Trannsport.

RAIL_Carbonfootprint = 0    #Pre-defining Variables
Rail_Use = 0                #Pre-defining Variables
Rail =  input(f"Have you taken any Railway Trips this {T[0:-2]} (Yes/No):")
#Steps taken to Make the Code More User Friendly and to overlook minor mistakes
Rail = Rail.strip()
Rail = Rail.lower()
#Evaluation
if Rail == "yes":
    Distance = float(input("Enter The Distance Travelled(Km):"))
    Logic_Check(Distance)     #Safety Measure Function Call   
    RAIL_Carbonfootprint=Distance*0.06                                  ##Final_Variable_07
    Rail_Use = True                                                     #Suggestion_Point_08
elif Rail == "no":                                                  
    Rail_Use = False
else:
    User_Is_BrainDed()       #Safety Measure Function Call   

print()        #This print() statement is written for the sake of making the terminal not look chaotic

#This parameter determines whether the user uses Bus Services as a mean of Trannsport.

BUS_Carbonfootprint = 0         #Pre-defining Variables
Bus_Use = 0                     #Pre-defining Variables
Bus =  input(f"Have you taken any Road Trips via Bus this {T[0:-2]} (Yes/No):")
#Steps taken to Make the Code More User Friendly and to overlook minor mistakes
Bus = Bus.strip()
Bus = Bus.lower()
#Evaluation
if Bus == "yes":
    Distance = float(input("Enter The Distance Travelled(km):"))
    Logic_Check(Distance)         #Safety Measure Function Call  
    BUS_Carbonfootprint=Distance*0.09                                   #Final_Variable_08
    Bus_Use = True                                                      #Suggestion_Point_09
elif Bus == "no":                                                      
    Bus_Use = False                                                  
else:
    User_Is_BrainDed()            #Safety Measure Function Call

print()            #This print() statement is written for the sake of making the terminal not look chaotic

#This Section of the the Code Deals With the Issue "if the User owns a vehicle or not"

Fuel_Kind = 0   #Pre-defining Variables
car = input("Do Own Any Vehicle that Runs on Pertrol/Diesel(Yes/No):")
#Steps taken to Make the Code More User Friendly and to overlook minor mistakes
car = car.strip()
car = car.lower()
#Evaluation
if car == "yes":
    Fuel_Type = input("Enter What Kind of Fuel Does Your Vehicle Consume(Diesel/Petrol):")
    #Steps taken to Make the Code More User Friendly and to overlook minor mistakes
    Fuel_Type = Fuel_Type.strip()
    Fuel_Type = Fuel_Type.lower()
    #Inner Evaluation
    if Fuel_Type == "diesel":
        Fuel_Kind = 2.6
    elif Fuel_Type == "petrol":
        Fuel_Kind = 2.3
    else:
        User_Is_BrainDed()    #Safety Measure Function Call

print()          #This print() statement is written for the sake of making the terminal not look chaotic

CAR_Carbonfootprint = 0  #Pre-defining Variables

if Fuel_Kind != 0 :
    Car =  input(f"Have you tarvelled in that Car Anytime this {T[0:-2]} (Yes/No):")
    #Steps taken to Make the Code More User Friendly and to overlook minor mistakes
    Car = Car.strip()
    Car = Car.lower()
    #Evaluation
    if Car == "yes":
        Distance = float(input("Enter The Distance Travelled:"))
        Logic_Check(Distance)
        CAR_Carbonfootprint=(Distance*Fuel_Kind)/Family_Members                               #Final_Variable_09
        Private_Transport = True                                                              #Suggestion_Point_10                
    elif Car == "no":                                                                
         Private_Transport = False
    else:
        User_Is_BrainDed()     #Safety Measure Function Call
else:
    Private_Transport = False

print()       #This print() statement is written for the sake of making the terminal not look chaotic

#Generation of Results  for Transportation
Total_CarbonFooprint_Transportation=PLANE_CarbonFootprint+RAIL_Carbonfootprint+BUS_Carbonfootprint+(CAR_Carbonfootprint/Family_Members)
Round_off(Total_CarbonFooprint_Transportation,3,Total_CarbonFooprint_Transportation)
TOTAL_CARBONFOOTPRINT = Total_CarbonFooprint_Transportation+Family_CarbonFootprint_FuelCinsumption
Round_off(TOTAL_CARBONFOOTPRINT,3,TOTAL_CARBONFOOTPRINT)

#Geneartion of Final Results
print("Results:")
if Live_Alone == True:
    print(f"Your Total CarbonFootprint produced due to your {T} Fuel Consumptions Is Estimated to be Around = {Total_CarbonFooprint_FuelConsumption}kg" )
else :
    print(f"Your Individual CarbonFootprint produced due to your {T} Fuel Consumptions Is Estimated to be Around = {Family_CarbonFootprint_FuelCinsumption}Kg")
print()
print(f"Your Individual CarbonFootprint produced due to your {T} Transportation Is Estimated to be Around = {Total_CarbonFooprint_Transportation}Kg")
print()
print(f"Now,The Total Carbon Footprint produced by your individual Acivities is Estimated to be around {TOTAL_CARBONFOOTPRINT}Kg")


Indian_Average = 1.2
UK_Average = 5.4
US_Average = 16

print("""
Average Carbon Footprints of Different Countries:
Indian_Average = 1.2 Tonnes
UK_Average = 5.4 Tonnes
US_Average = 16 Tonnes
""")
#Comparision of Carbon Footprints in Various Parts of the World
Kilogram_To_Tonnes(TOTAL_CARBONFOOTPRINT)
if c<=Indian_Average:
    print("Your average CarbnFootprint Does not exceeds the limit of an average Indian")
elif c>Indian_Average and c<=UK_Average:
    print("Your average CarbonFootprint exceeds that of an Average Indian")
elif c>UK_Average and c<US_Average:
    print("Your average CarbonFootprint exceeds that of a European citizen")
else:
    print("You Should take some measures to bring down your average Carbon Emission Immediately!")

print()         #This print() statement is written for the sake of making the terminal not look chaotic

print("Here are some personalised Reccomendations only for you to lead a more happy and green life:-")    
print()      

##Personalised_Recomendation_System

if Coal_Use == True or Coke_Use == True or Wood_Use == True:
    if Lpg_Use == False:
        print(f"Try Shift Your Fuel Source to LPG")
    if Lpg_Use == True:
        print(f"Try Shift Your Fuel Source 'Completely' to LPG")
elif Lpg_Use == True and (Coal_Use==False and Coal_Use == False and Wood_Use == False):
    print(f"Try New modes of Fuels like Electricity for household works(For Ex.Induction Cooker,Geysers,etc)")
if Plane_Use_Excess == True:
    print("Try to use Reduce Air Travels,Travel more by land in Other Public Vehicles")
if Private_Transport == True:
    print("Try Using Public Transports By land such as:-")
    if Rail_Use == False:
            print("Railway Services")
    elif Bus_Use == False:
            print("Bus Services")
    elif Rail_Use == True and Bus_Use == True:
            print("Both Railway and Bus Services More Frequently")
print("Reduce,Reuse and Recycle")

# Limitations of this project in the current situation :-

# The data produced can always be more accurrate
# The values of the Carbon Emission Factors keeps on changing from region to region and from place to place
# To make a huge effect on the society,A Dynamic Website is required which is not possible due to lack of resources
# The UI Proposal that would be incorported into the Future Website may be visually appealing but the current UI is very poor as it confined to the terminal place
# More Aspects of our daily lifestyles can be questioned for more accurate value for the User's Carbon Footprint but the CMF of many such factors are not known
