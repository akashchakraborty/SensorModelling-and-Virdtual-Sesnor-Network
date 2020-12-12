# Analog to digital converter files for 10,12 and 8 bit ADC
def adc_10(Vref):
    
    res= Vref/(2**10)
    return 1/res

def adc_12(Vref):
    
    res= Vref/(2**12)
    return 1/res

def adc_8(Vref):
    
    res= Vref/(2**8)
    return 1/res

