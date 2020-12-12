import random
import matplotlib.pyplot as plt
import numpy as np
def humidity(x,temp):
    if (temp<5 or temp>50):
        print("The temp is not in range of working condition for this sensor\nYou will not get favourable results!")
        x=x+random.choice([3.0,-3.0])
        adc_out=(x*((2**14)-2))/100
        adc_out=round(adc_out,2)
        mes_hum=(adc_out/((2**14)-2))*100
        return adc_out,mes_hum
    else:
        x=x+random.choice([3.0,-3.0])
        adc_out=(x*((2**14)-2))/100
        adc_out=round(adc_out,2)
        mes_hum=(adc_out/((2**14)-2))*100
        return adc_out,mes_hum

# adcOut,hum=humidity(20,26)
# print(hum)
# print(adcOut)
################################### testing ##############################################
def test_sensor_humid():
    
    hum=[25,30,30,31,33,33,33,35,37,37,41,40,30,30,30,31,33,33,33,35,37,37,41,40]
    mHum=[]
    t=np.arange(0,24,1)
    for i in hum:
        x,y=humidity(i,35)
        mHum.append(y)
    #print(mHum)
    
    plt.plot(t,mHum,label='measured')
    plt.plot(t,hum,label='original')
    plt.legend()
    plt.show()
 
#test_sensor_humid()