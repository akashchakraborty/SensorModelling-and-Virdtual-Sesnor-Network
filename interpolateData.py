import pandas as pd
# The following function will interpolate data and store it as data.csv
def interpolate_data(d):

    data=pd.read_csv(d)
    x=data.interpolate(method ='quadratic', limit_direction ='forward')
    print(x)
    name=input("By what file name would you like to save the interpolated dataset ?\n")
    x.to_csv(name,index=False) # writing the corrected CSV file
# testing
file=input("Enter the file you want to interpolate\n")
data=file # taking the input

interpolate_data(data)
