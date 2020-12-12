from LM35_v2 import lm35
from mq2 import SmokeSensor
from humidity import humidity

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np



def guwahati_annual_temp():
    
    data=pd.read_csv('guwa_final.csv')
    guwa_max_temp=data['MAX_T'].values.tolist()
    guwa_min_temp=data['MIN_T'].values.tolist()
    guwa_hum=data['HUM'].values.tolist()
    guwa_smoke=data['SMOKE'].values.tolist()
    #t=data['DAY'].values.tolist()
    t=np.arange(1,366,1)
    ###### agartala max temp ##########
    ov_guwa_tmax=[]
    for i in range(len(guwa_max_temp)):
        x=lm35(guwa_max_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        ov_guwa_tmax.append(x)
    #print(guwa_max_temp)
    out_tmax=[]
    for i in range(len(ov_guwa_tmax)):
        t_out=(ov_guwa_tmax[i]*204.8)*(500/1024)
        out_tmax.append(round(t_out,2))
    #print(out_tmax)

    ###### agartala min temp ##########
    ov_guwa_tmin=[]
    for i in range(len(guwa_min_temp)):
        x=lm35(guwa_min_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        ov_guwa_tmin.append(x)
    #print(guwa_min_temp)
    out_tmin=[]
    for i in range(len(ov_guwa_tmin)):
        t_out=(ov_guwa_tmin[i]*204.8)*(500/1024)
        out_tmin.append(round(t_out,2))

    return guwa_max_temp, guwa_min_temp, out_tmin, out_tmax

def guwahati_annual_hum():
    data=pd.read_csv('guwa_final.csv')
    guwa_hum=data['HUM'].values.tolist()
    mHum=[]
    for i in guwa_hum :
        x,y=humidity(i,35)
        mHum.append(y)

    return guwa_hum, mHum

def guwahati_annual_smoke():
    data=pd.read_csv('guwa_final.csv')
    guwa_smoke=data['SMOKE'].values.tolist()
    ppm=[]
    voutSmoke=[]
    for i in guwa_smoke:
        out,ratio=SmokeSensor(i,5,5000)
        voutSmoke.append(out)
    for j in voutSmoke:
        rs=((5/j)-1)*5000
        g=(2.1217-(rs/3600))/0.00015
        g=round(g,3)
        ppm.append(g)
    return guwa_smoke, ppm