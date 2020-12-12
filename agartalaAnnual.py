from LM35_v2 import lm35
from mq2 import SmokeSensor
from humidity import humidity

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

def agartala_annual_temp():
    data=pd.read_csv('agar_final.csv')
    agar_max_temp=data['MAX_T'].values.tolist()
    agar_min_temp=data['MIN_T'].values.tolist()
    agar_hum=data['HUM'].values.tolist()
    agar_smoke=data['SMOKE'].values.tolist()
    #t=data['DAY'].values.tolist()
    t=np.arange(1,366,1)
    ###### agartala max temp ##########
    ov_agar_tmax=[]
    for i in range(len(agar_max_temp)):
        x=lm35(agar_max_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        ov_agar_tmax.append(x)
    #print(agar_max_temp)
    out_tmax=[]
    for i in range(len(ov_agar_tmax)):
        t_out=(ov_agar_tmax[i]*204.8)*(500/1024)
        out_tmax.append(round(t_out,2))
    #print(out_tmax)

    ###### agartala min temp ##########
    ov_agar_tmin=[]
    for i in range(len(agar_min_temp)):
        x=lm35(agar_min_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        ov_agar_tmin.append(x)
    #print(agar_min_temp)
    out_tmin=[]
    for i in range(len(ov_agar_tmin)):
        t_out=(ov_agar_tmin[i]*204.8)*(500/1024)
        out_tmin.append(round(t_out,2))

    return agar_max_temp, agar_min_temp, out_tmin, out_tmax

def agartala_annual_hum():
    data=pd.read_csv('agar_final.csv')
    agar_hum=data['HUM'].values.tolist()
    mHum=[]
    for i in agar_hum :
        x,y=humidity(i,35)
        mHum.append(y)

    return agar_hum, mHum

def agartala_annual_smoke():
    data=pd.read_csv('agar_final.csv')
    agar_smoke=data['SMOKE'].values.tolist()
    ppm=[]
    voutSmoke=[]
    for i in agar_smoke:
        out,ratio=SmokeSensor(i,5,5000)
        voutSmoke.append(out)
    for j in voutSmoke:
        rs=((5/j)-1)*5000
        g=(2.1217-(rs/3600))/0.00015
        g=round(g,3)
        ppm.append(g)
    return agar_smoke, ppm