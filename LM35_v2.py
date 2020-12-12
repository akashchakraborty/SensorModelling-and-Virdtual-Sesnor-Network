import random

def lm35(x,Vs,I_load):
    if x==-55.0 or x==150.0:
        in_temp=x+random.choice([-1.1,1.1]) # Ta=Tmin=Tmax then +-0.8 & +-0.3
    elif x==25.0:
        in_temp=x+random.choice([-0.7,0.7]) # Ta=25 , +- 0.4 & +-0.3
    elif x== -10.0:
        in_temp=x+random.choice([-0.8,0.8]) # Ta=-10 , +- 0.5 & +-0.3
    elif x==0:
        in_temp=x+0.3
    else:
        in_temp=x+random.choice([-0.3,0.3]) # Tmin<Ta<Tmax  +-0.3
    #print(in_temp)
    # Vout affected by Line and Load Regulation 
    vout=(10*in_temp)+(random.choice([-0.02,0.02])*Vs)+(random.choice([-0.5,0.5])*(I_load))
    
    return vout

