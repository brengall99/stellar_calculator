import pandas as pd

df = pd.read_csv('ROOT.csv')

def get_plan(arpu):
    return min(common_list, key=lambda x:abs(x-float(arpu)))
    
df["Suggested plan"] = df["ARPU"].apply(get_plan)
df.to_csv('ROOT.csv')