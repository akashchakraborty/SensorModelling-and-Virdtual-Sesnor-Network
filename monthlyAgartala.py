import pandas as pd 
from LM35_v2 import lm35
from mq2 import SmokeSensor
from humidity import humidity

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np


data=pd.read_csv('agar_final.csv')
jan=data.loc[0:30]
feb=data.loc[31:58]
march = data.loc[59:89]
april=data.loc[90:119]
may=data.loc[120:150]
june = data.loc[151:180]
july=data.loc[181:211]
aug=data.loc[212:242]
sept = data.loc[243:272]
octo=data.loc[273:303]
nov=data.loc[304:333]
dec = data.loc[334:364]

def jan_data_agar():

    jan_agar_max_temp=jan['MAX_T'].values.tolist()
    jan_agar_min_temp=jan['MIN_T'].values.tolist()
    jan_agar_hum=jan['HUM'].values.tolist()
    jan_agar_smoke=jan['SMOKE'].values.tolist()
## temperature ###
    jan_ov_agar_tmax=[]
    for i in range(len(jan_agar_max_temp)):
        x=lm35(jan_agar_max_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        jan_ov_agar_tmax.append(x)
    #print(agar_max_temp)
    jan_out_tmax=[]
    for i in range(len(jan_ov_agar_tmax)):
        t_out=(jan_ov_agar_tmax[i]*204.8)*(500/1024)
        jan_out_tmax.append(round(t_out,2))

    jan_ov_agar_tmin=[]
    for i in range(len(jan_agar_min_temp)):
        x=lm35(jan_agar_min_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        jan_ov_agar_tmin.append(x)
    #print(agar_min_temp)
    jan_out_tmin=[]
    for i in range(len(jan_ov_agar_tmin)):
        t_out=(jan_ov_agar_tmin[i]*204.8)*(500/1024)
        jan_out_tmin.append(round(t_out,2))
#### humidity

    jan_mHum=[]
    for i in jan_agar_hum :
        x,y=humidity(i,35)
        jan_mHum.append(y)
    
### smoke
    jan_ppm=[]
    voutSmoke=[]
    for i in jan_agar_smoke:
        out,ratio=SmokeSensor(i,5,5000)
        voutSmoke.append(out)
    for j in voutSmoke:
        rs=((5/j)-1)*5000
        g=(2.1217-(rs/3600))/0.00015
        g=round(g,3)
        jan_ppm.append(g)

    return jan_out_tmax,jan_out_tmin,jan_mHum,jan_ppm



def feb_data_agar():

    feb_agar_max_temp=feb['MAX_T'].values.tolist()
    feb_agar_min_temp=feb['MIN_T'].values.tolist()
    feb_agar_hum=feb['HUM'].values.tolist()
    feb_agar_smoke=feb['SMOKE'].values.tolist()
## temperature ###
    feb_ov_agar_tmax=[]
    for i in range(len(feb_agar_max_temp)):
        x=lm35(feb_agar_max_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        feb_ov_agar_tmax.append(x)
    #print(agar_max_temp)
    feb_out_tmax=[]
    for i in range(len(feb_ov_agar_tmax)):
        t_out=(feb_ov_agar_tmax[i]*204.8)*(500/1024)
        feb_out_tmax.append(round(t_out,2))

    feb_ov_agar_tmin=[]
    for i in range(len(feb_agar_min_temp)):
        x=lm35(feb_agar_min_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        feb_ov_agar_tmin.append(x)
    #print(agar_min_temp)
    feb_out_tmin=[]
    for i in range(len(feb_ov_agar_tmin)):
        t_out=(feb_ov_agar_tmin[i]*204.8)*(500/1024)
        feb_out_tmin.append(round(t_out,2))
#### humidity

    feb_mHum=[]
    for i in feb_agar_hum :
        x,y=humidity(i,35)
        feb_mHum.append(y)
    
### smoke
    feb_ppm=[]
    voutSmoke=[]
    for i in feb_agar_smoke:
        out,ratio=SmokeSensor(i,5,5000)
        voutSmoke.append(out)
    for j in voutSmoke:
        rs=((5/j)-1)*5000
        g=(2.1217-(rs/3600))/0.00015
        g=round(g,3)
        feb_ppm.append(g)

    return feb_out_tmax,feb_out_tmin,feb_mHum,feb_ppm




def march_data_agar():

    march_agar_max_temp=march['MAX_T'].values.tolist()
    march_agar_min_temp=march['MIN_T'].values.tolist()
    march_agar_hum=march['HUM'].values.tolist()
    march_agar_smoke=march['SMOKE'].values.tolist()
## temperature ###
    march_ov_agar_tmax=[]
    for i in range(len(march_agar_max_temp)):
        x=lm35(march_agar_max_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        march_ov_agar_tmax.append(x)
    #print(agar_max_temp)
    march_out_tmax=[]
    for i in range(len(march_ov_agar_tmax)):
        t_out=(march_ov_agar_tmax[i]*204.8)*(500/1024)
        march_out_tmax.append(round(t_out,2))

    march_ov_agar_tmin=[]
    for i in range(len(march_agar_min_temp)):
        x=lm35(march_agar_min_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        march_ov_agar_tmin.append(x)
    #print(agar_min_temp)
    march_out_tmin=[]
    for i in range(len(march_ov_agar_tmin)):
        t_out=(march_ov_agar_tmin[i]*204.8)*(500/1024)
        march_out_tmin.append(round(t_out,2))
#### humidity

    march_mHum=[]
    for i in march_agar_hum :
        x,y=humidity(i,35)
        march_mHum.append(y)
    
### smoke
    march_ppm=[]
    voutSmoke=[]
    for i in march_agar_smoke:
        out,ratio=SmokeSensor(i,5,5000)
        voutSmoke.append(out)
    for j in voutSmoke:
        rs=((5/j)-1)*5000
        g=(2.1217-(rs/3600))/0.00015
        g=round(g,3)
        march_ppm.append(g)

    return march_out_tmax,march_out_tmin,march_mHum,march_ppm





def april_data_agar():

    april_agar_max_temp=april['MAX_T'].values.tolist()
    april_agar_min_temp=april['MIN_T'].values.tolist()
    april_agar_hum=april['HUM'].values.tolist()
    april_agar_smoke=april['SMOKE'].values.tolist()
## temperature ###
    april_ov_agar_tmax=[]
    for i in range(len(april_agar_max_temp)):
        x=lm35(april_agar_max_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        april_ov_agar_tmax.append(x)
    #print(agar_max_temp)
    april_out_tmax=[]
    for i in range(len(april_ov_agar_tmax)):
        t_out=(april_ov_agar_tmax[i]*204.8)*(500/1024)
        april_out_tmax.append(round(t_out,2))

    april_ov_agar_tmin=[]
    for i in range(len(april_agar_min_temp)):
        x=lm35(april_agar_min_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        april_ov_agar_tmin.append(x)
    #print(agar_min_temp)
    april_out_tmin=[]
    for i in range(len(april_ov_agar_tmin)):
        t_out=(april_ov_agar_tmin[i]*204.8)*(500/1024)
        april_out_tmin.append(round(t_out,2))
#### humidity

    april_mHum=[]
    for i in april_agar_hum :
        x,y=humidity(i,35)
        april_mHum.append(y)
    
### smoke
    april_ppm=[]
    voutSmoke=[]
    for i in april_agar_smoke:
        out,ratio=SmokeSensor(i,5,5000)
        voutSmoke.append(out)
    for j in voutSmoke:
        rs=((5/j)-1)*5000
        g=(2.1217-(rs/3600))/0.00015
        g=round(g,3)
        april_ppm.append(g)

    return april_out_tmax,april_out_tmin,april_mHum,april_ppm

def may_data_agar():

    may_agar_max_temp=may['MAX_T'].values.tolist()
    may_agar_min_temp=may['MIN_T'].values.tolist()
    may_agar_hum=may['HUM'].values.tolist()
    may_agar_smoke=may['SMOKE'].values.tolist()
## temperature ###
    may_ov_agar_tmax=[]
    for i in range(len(may_agar_max_temp)):
        x=lm35(may_agar_max_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        may_ov_agar_tmax.append(x)
    #print(agar_max_temp)
    may_out_tmax=[]
    for i in range(len(may_ov_agar_tmax)):
        t_out=(may_ov_agar_tmax[i]*204.8)*(500/1024)
        may_out_tmax.append(round(t_out,2))

    may_ov_agar_tmin=[]
    for i in range(len(may_agar_min_temp)):
        x=lm35(may_agar_min_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        may_ov_agar_tmin.append(x)
    #print(agar_min_temp)
    may_out_tmin=[]
    for i in range(len(may_ov_agar_tmin)):
        t_out=(may_ov_agar_tmin[i]*204.8)*(500/1024)
        may_out_tmin.append(round(t_out,2))
#### humidity

    may_mHum=[]
    for i in may_agar_hum :
        x,y=humidity(i,35)
        may_mHum.append(y)
    
### smoke
    may_ppm=[]
    voutSmoke=[]
    for i in may_agar_smoke:
        out,ratio=SmokeSensor(i,5,5000)
        voutSmoke.append(out)
    for j in voutSmoke:
        rs=((5/j)-1)*5000
        g=(2.1217-(rs/3600))/0.00015
        g=round(g,3)
        may_ppm.append(g)

    return may_out_tmax,may_out_tmin,may_mHum,may_ppm


def june_data_agar():

    june_agar_max_temp=june['MAX_T'].values.tolist()
    june_agar_min_temp=june['MIN_T'].values.tolist()
    june_agar_hum=june['HUM'].values.tolist()
    june_agar_smoke=june['SMOKE'].values.tolist()
## temperature ###
    june_ov_agar_tmax=[]
    for i in range(len(june_agar_max_temp)):
        x=lm35(june_agar_max_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        june_ov_agar_tmax.append(x)
    #print(agar_max_temp)
    june_out_tmax=[]
    for i in range(len(june_ov_agar_tmax)):
        t_out=(june_ov_agar_tmax[i]*204.8)*(500/1024)
        june_out_tmax.append(round(t_out,2))

    june_ov_agar_tmin=[]
    for i in range(len(june_agar_min_temp)):
        x=lm35(june_agar_min_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        june_ov_agar_tmin.append(x)
    #print(agar_min_temp)
    june_out_tmin=[]
    for i in range(len(june_ov_agar_tmin)):
        t_out=(june_ov_agar_tmin[i]*204.8)*(500/1024)
        june_out_tmin.append(round(t_out,2))
#### humidity

    june_mHum=[]
    for i in june_agar_hum :
        x,y=humidity(i,35)
        june_mHum.append(y)
    
### smoke
    june_ppm=[]
    voutSmoke=[]
    for i in june_agar_smoke:
        out,ratio=SmokeSensor(i,5,5000)
        voutSmoke.append(out)
    for j in voutSmoke:
        rs=((5/j)-1)*5000
        g=(2.1217-(rs/3600))/0.00015
        g=round(g,3)
        june_ppm.append(g)

    return june_out_tmax,june_out_tmin,june_mHum,june_ppm


def july_data_agar():

    july_agar_max_temp=july['MAX_T'].values.tolist()
    july_agar_min_temp=july['MIN_T'].values.tolist()
    july_agar_hum=july['HUM'].values.tolist()
    july_agar_smoke=july['SMOKE'].values.tolist()
## temperature ###
    july_ov_agar_tmax=[]
    for i in range(len(july_agar_max_temp)):
        x=lm35(july_agar_max_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        july_ov_agar_tmax.append(x)
    #print(agar_max_temp)
    july_out_tmax=[]
    for i in range(len(july_ov_agar_tmax)):
        t_out=(july_ov_agar_tmax[i]*204.8)*(500/1024)
        july_out_tmax.append(round(t_out,2))

    july_ov_agar_tmin=[]
    for i in range(len(july_agar_min_temp)):
        x=lm35(july_agar_min_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        july_ov_agar_tmin.append(x)
    #print(agar_min_temp)
    july_out_tmin=[]
    for i in range(len(july_ov_agar_tmin)):
        t_out=(july_ov_agar_tmin[i]*204.8)*(500/1024)
        july_out_tmin.append(round(t_out,2))
#### humidity

    july_mHum=[]
    for i in july_agar_hum :
        x,y=humidity(i,35)
        july_mHum.append(y)
    
### smoke
    july_ppm=[]
    voutSmoke=[]
    for i in july_agar_smoke:
        out,ratio=SmokeSensor(i,5,5000)
        voutSmoke.append(out)
    for j in voutSmoke:
        rs=((5/j)-1)*5000
        g=(2.1217-(rs/3600))/0.00015
        g=round(g,3)
        july_ppm.append(g)

    return july_out_tmax,july_out_tmin,july_mHum,july_ppm


def aug_data_agar():

    aug_agar_max_temp=aug['MAX_T'].values.tolist()
    aug_agar_min_temp=aug['MIN_T'].values.tolist()
    aug_agar_hum=aug['HUM'].values.tolist()
    aug_agar_smoke=aug['SMOKE'].values.tolist()
## temperature ###
    aug_ov_agar_tmax=[]
    for i in range(len(aug_agar_max_temp)):
        x=lm35(aug_agar_max_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        aug_ov_agar_tmax.append(x)
    #print(agar_max_temp)
    aug_out_tmax=[]
    for i in range(len(aug_ov_agar_tmax)):
        t_out=(aug_ov_agar_tmax[i]*204.8)*(500/1024)
        aug_out_tmax.append(round(t_out,2))

    aug_ov_agar_tmin=[]
    for i in range(len(aug_agar_min_temp)):
        x=lm35(aug_agar_min_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        aug_ov_agar_tmin.append(x)
    #print(agar_min_temp)
    aug_out_tmin=[]
    for i in range(len(aug_ov_agar_tmin)):
        t_out=(aug_ov_agar_tmin[i]*204.8)*(500/1024)
        aug_out_tmin.append(round(t_out,2))
#### humidity

    aug_mHum=[]
    for i in aug_agar_hum :
        x,y=humidity(i,35)
        aug_mHum.append(y)
    
### smoke
    aug_ppm=[]
    voutSmoke=[]
    for i in aug_agar_smoke:
        out,ratio=SmokeSensor(i,5,5000)
        voutSmoke.append(out)
    for j in voutSmoke:
        rs=((5/j)-1)*5000
        g=(2.1217-(rs/3600))/0.00015
        g=round(g,3)
        aug_ppm.append(g)

    return aug_out_tmax,aug_out_tmin,aug_mHum,aug_ppm


def sept_data_agar():

    sept_agar_max_temp=sept['MAX_T'].values.tolist()
    sept_agar_min_temp=sept['MIN_T'].values.tolist()
    sept_agar_hum=sept['HUM'].values.tolist()
    sept_agar_smoke=sept['SMOKE'].values.tolist()
## temperature ###
    sept_ov_agar_tmax=[]
    for i in range(len(sept_agar_max_temp)):
        x=lm35(sept_agar_max_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        sept_ov_agar_tmax.append(x)
    #print(agar_max_temp)
    sept_out_tmax=[]
    for i in range(len(sept_ov_agar_tmax)):
        t_out=(sept_ov_agar_tmax[i]*204.8)*(500/1024)
        sept_out_tmax.append(round(t_out,2))

    sept_ov_agar_tmin=[]
    for i in range(len(sept_agar_min_temp)):
        x=lm35(sept_agar_min_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        sept_ov_agar_tmin.append(x)
    #print(agar_min_temp)
    sept_out_tmin=[]
    for i in range(len(sept_ov_agar_tmin)):
        t_out=(sept_ov_agar_tmin[i]*204.8)*(500/1024)
        sept_out_tmin.append(round(t_out,2))
#### humidity

    sept_mHum=[]
    for i in sept_agar_hum :
        x,y=humidity(i,35)
        sept_mHum.append(y)
    
### smoke
    sept_ppm=[]
    voutSmoke=[]
    for i in sept_agar_smoke:
        out,ratio=SmokeSensor(i,5,5000)
        voutSmoke.append(out)
    for j in voutSmoke:
        rs=((5/j)-1)*5000
        g=(2.1217-(rs/3600))/0.00015
        g=round(g,3)
        sept_ppm.append(g)

    return sept_out_tmax,sept_out_tmin,sept_mHum,sept_ppm


def octo_data_agar():

    octo_agar_max_temp=octo['MAX_T'].values.tolist()
    octo_agar_min_temp=octo['MIN_T'].values.tolist()
    octo_agar_hum=octo['HUM'].values.tolist()
    octo_agar_smoke=octo['SMOKE'].values.tolist()
## temperature ###
    octo_ov_agar_tmax=[]
    for i in range(len(octo_agar_max_temp)):
        x=lm35(octo_agar_max_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        octo_ov_agar_tmax.append(x)
    #print(agar_max_temp)
    octo_out_tmax=[]
    for i in range(len(octo_ov_agar_tmax)):
        t_out=(octo_ov_agar_tmax[i]*204.8)*(500/1024)
        octo_out_tmax.append(round(t_out,2))

    octo_ov_agar_tmin=[]
    for i in range(len(octo_agar_min_temp)):
        x=lm35(octo_agar_min_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        octo_ov_agar_tmin.append(x)
    #print(agar_min_temp)
    octo_out_tmin=[]
    for i in range(len(octo_ov_agar_tmin)):
        t_out=(octo_ov_agar_tmin[i]*204.8)*(500/1024)
        octo_out_tmin.append(round(t_out,2))
#### humidity

    octo_mHum=[]
    for i in octo_agar_hum :
        x,y=humidity(i,35)
        octo_mHum.append(y)
    
### smoke
    octo_ppm=[]
    voutSmoke=[]
    for i in octo_agar_smoke:
        out,ratio=SmokeSensor(i,5,5000)
        voutSmoke.append(out)
    for j in voutSmoke:
        rs=((5/j)-1)*5000
        g=(2.1217-(rs/3600))/0.00015
        g=round(g,3)
        octo_ppm.append(g)

    return octo_out_tmax,octo_out_tmin,octo_mHum,octo_ppm


def nov_data_agar():

    nov_agar_max_temp=nov['MAX_T'].values.tolist()
    nov_agar_min_temp=nov['MIN_T'].values.tolist()
    nov_agar_hum=nov['HUM'].values.tolist()
    nov_agar_smoke=nov['SMOKE'].values.tolist()
## temperature ###
    nov_ov_agar_tmax=[]
    for i in range(len(nov_agar_max_temp)):
        x=lm35(nov_agar_max_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        nov_ov_agar_tmax.append(x)
    #print(agar_max_temp)
    nov_out_tmax=[]
    for i in range(len(nov_ov_agar_tmax)):
        t_out=(nov_ov_agar_tmax[i]*204.8)*(500/1024)
        nov_out_tmax.append(round(t_out,2))

    nov_ov_agar_tmin=[]
    for i in range(len(nov_agar_min_temp)):
        x=lm35(nov_agar_min_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        nov_ov_agar_tmin.append(x)
    #print(agar_min_temp)
    nov_out_tmin=[]
    for i in range(len(nov_ov_agar_tmin)):
        t_out=(nov_ov_agar_tmin[i]*204.8)*(500/1024)
        nov_out_tmin.append(round(t_out,2))
#### humidity

    nov_mHum=[]
    for i in nov_agar_hum :
        x,y=humidity(i,35)
        nov_mHum.append(y)
    
### smoke
    nov_ppm=[]
    voutSmoke=[]
    for i in nov_agar_smoke:
        out,ratio=SmokeSensor(i,5,5000)
        voutSmoke.append(out)
    for j in voutSmoke:
        rs=((5/j)-1)*5000
        g=(2.1217-(rs/3600))/0.00015
        g=round(g,3)
        nov_ppm.append(g)

    return nov_out_tmax,nov_out_tmin,nov_mHum,nov_ppm


def dec_data_agar():

    dec_agar_max_temp=dec['MAX_T'].values.tolist()
    dec_agar_min_temp=dec['MIN_T'].values.tolist()
    dec_agar_hum=dec['HUM'].values.tolist()
    dec_agar_smoke=dec['SMOKE'].values.tolist()
## temperature ###
    dec_ov_agar_tmax=[]
    for i in range(len(dec_agar_max_temp)):
        x=lm35(dec_agar_max_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        dec_ov_agar_tmax.append(x)
    #print(agar_max_temp)
    dec_out_tmax=[]
    for i in range(len(dec_ov_agar_tmax)):
        t_out=(dec_ov_agar_tmax[i]*204.8)*(500/1024)
        dec_out_tmax.append(round(t_out,2))

    dec_ov_agar_tmin=[]
    for i in range(len(dec_agar_min_temp)):
        x=lm35(dec_agar_min_temp[i],5,1) #temp,Volts,MilliAmps
        x=x/1000
        x=round(x,3)
        dec_ov_agar_tmin.append(x)
    #print(agar_min_temp)
    dec_out_tmin=[]
    for i in range(len(dec_ov_agar_tmin)):
        t_out=(dec_ov_agar_tmin[i]*204.8)*(500/1024)
        dec_out_tmin.append(round(t_out,2))
#### humidity

    dec_mHum=[]
    for i in dec_agar_hum :
        x,y=humidity(i,35)
        dec_mHum.append(y)
    
### smoke
    dec_ppm=[]
    voutSmoke=[]
    for i in dec_agar_smoke:
        out,ratio=SmokeSensor(i,5,5000)
        voutSmoke.append(out)
    for j in voutSmoke:
        rs=((5/j)-1)*5000
        g=(2.1217-(rs/3600))/0.00015
        g=round(g,3)
        dec_ppm.append(g)

    return dec_out_tmax,dec_out_tmin,dec_mHum,dec_ppm