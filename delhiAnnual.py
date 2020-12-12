from LM35_v2 import lm35
from mq2 import SmokeSensor
from humidity import humidity

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np


def delhi_annual_temp():
    data=pd.read_csv('del_final.csv')
    del_max_temp=data['MAX_T'].values.tolist()
    del_min_temp=data['MIN_T'].values.tolist()
    del_hum=data['HUM'].values.tolist()
    del_smoke=data['SMOKE'].values.tolist()
    #t=data['DAY'].values.tolist()
    t=np.arange(1,366,1)
    ###### delhi max temp ##########
    ov_del_tmax=[]
    for i in range(len(del_max_temp)):
        x=lm35(del_max_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        ov_del_tmax.append(x)
    #print(del_max_temp)
    out_tmax=[]
    for i in range(len(ov_del_tmax)):
        t_out=(ov_del_tmax[i]*204.8)*(500/1024)
        out_tmax.append(round(t_out,2))
    #print(out_tmax)

    ###### delhi min temp ##########
    ov_del_tmin=[]
    for i in range(len(del_min_temp)):
        x=lm35(del_min_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        ov_del_tmin.append(x)
    #print(del_min_temp)
    out_tmin=[]
    for i in range(len(ov_del_tmin)):
        t_out=(ov_del_tmin[i]*204.8)*(500/1024)
        out_tmin.append(round(t_out,2))


    return del_max_temp, del_min_temp, out_tmin, out_tmax

def delhi_annual_hum():
    data=pd.read_csv('del_final.csv')
    del_hum=data['HUM'].values.tolist()
    mHum=[]
    for i in del_hum :
        x,y=humidity(i,35)
        mHum.append(y)

    return del_hum, mHum

def delhi_annual_smoke():
    data=pd.read_csv('del_final.csv')
    del_smoke=data['SMOKE'].values.tolist()
    ppm=[]
    voutSmoke=[]
    for i in del_smoke:
        out,ratio=SmokeSensor(i,5,5000)
        voutSmoke.append(out)
    for j in voutSmoke:
        rs=((5/j)-1)*5000
        g=(2.1217-(rs/3600))/0.00015
        g=round(g,3)
        ppm.append(g)
    return del_smoke, ppm