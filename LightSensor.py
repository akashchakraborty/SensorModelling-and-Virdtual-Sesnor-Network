###Resitance of photocell = 500 / Lux for a typical LDR###



import random
import math

def LightSensor(time):
    Input_Illumination = {'Sunlight': 107527, 'Full Day Light' : 10752, 'Overcast Day':1075, 'Very Dark Day':107, 'Twilight':10.8, 'Deep Twilight' : 1.08, 'Full Moon': .108, 'Quarter Moon' : 0.0108, 'Star Light':0.0011,'Overcast Night':0.0001}
    Time = Input_Illumination.get(time)
    Sensitivity = 0.8

    Input_Voltage = 5

    
    Photocell_Resistance1 = (500/(Time))*1000*Sensitivity
    Vo=Input_Voltage*(Photocell_Resistance1/(Photocell_Resistance1+3300))

    #print (Photocell_Resistance1, "ohms is the LDR Resistance for Illumination =", Time, "lux" )
    return Vo, Photocell_Resistance1,Time

    #print(Vo)



##Selection = input("Enter the time")
##x,y = LightSensor(Selection)
##print(x)
##print(y)






