import pandas as pd

data = pd.read_csv("../RuDénom.csv",sep="\t")

unique = data[~data.duplicated(subset=['Nom'], keep=False)]
high_all = unique.loc[unique['FreqA'] >= 100]

print("High frequency all data:", high_all.shape[0])


high = high_all.dropna(subset=['Score_p'])

print("High frequency data for the study:", high.shape[0])

high.to_csv("HFreq_data.csv",sep='\t',index=False)