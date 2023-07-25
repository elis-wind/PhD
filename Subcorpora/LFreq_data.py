import pandas as pd

data = pd.read_csv("../RuDénom.csv",sep="\t")

unique = data[~data.duplicated(subset=['Nom'], keep=False)]
low_all = unique.loc[unique['FreqA'] == 1]

print("Low frequency all data:", low_all.shape[0])


low = low_all.dropna(subset=['Score_p'])

print("Low frequency data for the study:", low.shape[0])

low.to_csv("LFreq_data.csv",sep='\t',index=False)