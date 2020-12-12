

def SmokeSensor(x,Vs,rL):
    r0=3600 #r0=3.6k ohm
    t1=(-0.0001521*x*r0)
    t2=(2.1217*r0)
    rs=t1+t2
    vout= (Vs*rL)/(rs+rL)
    vout=round(vout,4)
    y=rs/r0 #rs/r0
    y=round(y,2)
    
    return vout,y

# x,y=SmokeSensor(10000,5,5000)
# print(y) #gives the rs/r0
# print(x) #gives the vout
  
def lpgSensor():
    pass

def methaneSensor():
    pass
