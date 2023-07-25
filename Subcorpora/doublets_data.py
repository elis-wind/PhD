import pandas as pd

data = pd.read_csv("../RuDénom.csv",sep="\t")

doublets = data[data.duplicated(subset=['Nom'],keep=False)]

print("Doublets data:", doublets.shape[0])

doublets.to_csv("doublets_data.csv",sep='\t',index=False)