from annual import *
import pandas as pd

def city():
    x=input('''
    Enter the city of your choice: 
    1. Delhi
    2. Agartala
    3. Guwahati\n
    ''')
    return x

def main():

    x = city()
    
    if x == "Delhi":
        delhi()
    elif x == "Agartala":
        agartala()
    elif x == "Guwahati":
        guwahati()
    elif x == "Mumbai":
        mumbai()
    else:
        print("In progress")
    
main()