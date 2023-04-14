import pandas as pd
file=pd.read_csv("F:\college\sem2\IR\sec\code\populationbycountry.csv")
new_file = file.dropna(axis=0 , how="any")
print("the file frame length:", len(file), "\nthe New file frame length:" , len(new_file), "\nNumber of rows with at least 1 null value: ",(len(file)-len(new_file)))
