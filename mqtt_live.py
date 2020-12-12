import paho.mqtt.client as mqtt

import time
from LM35_v2 import lm35
from mq2 import SmokeSensor
from humidity import humidity

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import random


def start_mqtt_live():

    mqttBroker="test.mosquitto.org"
    client = mqtt.Client("Akash-420")
    client.connect(mqttBroker)

    while True:

        temp_raw=random.uniform(0,50)
        hum_raw=random.uniform(10,90)
        ldr=random.uniform(0.0001,107527)
        smoke_raw=random.uniform(20,100)
    #### temp data
        temp=lm35(temp_raw,5,1)
        temp=temp/1000
        temp1=round(temp,3)
        temp=(temp1*204.8)*(500/1024)
        temp=round(temp,2)
    #### hum data
        x,hum=humidity(hum_raw,35)
    #### smoke data
        out,ratio=SmokeSensor(smoke_raw,5,5000)
        rs=((5/out)-1)*5000
        g=(2.1217-(rs/3600))/0.00015
        smoke=round(g,3)
    #### ldr data




        client.publish("Capstone Data Temperature",temp)
        client.publish("Capstone Data Humidity",hum)
        client.publish("Capstone Data LDR (Lux)",ldr)
        client.publish("Capstone Data Smoke",smoke)
        print("Just published"+str(temp)+" to the topic Capstone Data Temperature")
        print("Just published"+str(hum)+" to the topic Capstone Data Humidity")
        print("Just published"+str(ldr)+" to the topic Capstone Data LDR (Lux)")
        print("Just published"+str(smoke)+" to the topic Capstone Data Smoke")
        time.sleep(1)

start_mqtt_live()