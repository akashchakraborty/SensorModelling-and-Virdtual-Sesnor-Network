from LM35_v2 import lm35
from mq2 import SmokeSensor
from humidity import humidity

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

def convert_to_df(a1,a2,a3,a4):

    nump_arr = np.array([a1,a2,a3,a4])
    n_trans = np.transpose(nump_arr)
    data = pd.DataFrame(n_trans,columns=['MaxTemp','MinTemp','Humidity','Smoke'])
    return data

def delhi():
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
    #print(out_tmin)

    ####### delhi humidity ##########
    # mHum=[]
    # for i in range(len(del_hum)) :
    #     for j in range(i,len(del_max_temp)):
    #         x,y=humidity(del_hum[i],del_max_temp[j])
    #         mHum.append(y)
    #     break
    mHum=[]
    for i in del_hum :
        x,y=humidity(i,35)
        mHum.append(y)
    #print(mHum)

    ###### delhi smoke (PM2.5)
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
    #print("\n")
    #print(ppm)
    dataframe = convert_to_df(out_tmax,out_tmin,mHum,ppm)
    print(dataframe)

    ##### Plotting all the graphs -- max temp/min temp/humidity/PM 2.5
    # plt.subplot(221),plt.plot(t,out_tmax),plt.title('Max temp Annual')
    # plt.subplot(223),plt.plot(t,out_tmin),plt.title('Min temp Annual')
    # plt.subplot(222),plt.plot(t,mHum),plt.title('Humidity Annual')
    # plt.subplot(224),plt.plot(t,ppm),plt.title('Smoke/PM 2.5 Annual')

    # plt.show()

def agartala():
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
    #print(out_tmin)

    ####### agartala humidity ##########
    
    mHum=[]
    for i in agar_hum :
        x,y=humidity(i,35)
        mHum.append(y)

    #print(mHum)

    ###### agartala smoke (PM2.5)
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
    #print("\n")
    #print(ppm)
    dataframe = convert_to_df(out_tmax,out_tmin,mHum,ppm)
    print(dataframe)
    ##### Plotting all the graphs -- max temp/min temp/humidity/PM 2.5
    # plt.title('Agartala-Yearly-Data')
    # plt.subplot(221),plt.plot(t,out_tmax),plt.title('Max temp Annual')
    # plt.subplot(223),plt.plot(t,out_tmin),plt.title('Min temp Annual')
    # plt.subplot(222),plt.plot(t,mHum),plt.title('Humidity Annual')
    # plt.subplot(224),plt.plot(t,ppm),plt.title('Smoke/PM 2.5 Annual')
    
    #plt.show()


def guwahati():
    
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
    #print(out_tmin)

    ####### agartala humidity ##########
    
    mHum=[]
    for i in guwa_hum :
        x,y=humidity(i,35)
        mHum.append(y)

    #print(mHum)

    ###### agartala smoke (PM2.5)
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
    #print("\n")
    #print(ppm)
    dataframe = convert_to_df(out_tmax,out_tmin,mHum,ppm)
    print(dataframe)
    ##### Plotting all the graphs -- max temp/min temp/humidity/PM 2.5
    # plt.title('Agartala-Yearly-Data')
    # plt.subplot(221),plt.plot(t,out_tmax),plt.title('Max temp Annual')
    # plt.subplot(223),plt.plot(t,out_tmin),plt.title('Min temp Annual')
    # plt.subplot(222),plt.plot(t,mHum),plt.title('Humidity Annual')
    # plt.subplot(224),plt.plot(t,ppm),plt.title('Smoke/PM 2.5 Annual')
    
    #plt.show()