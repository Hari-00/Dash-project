import pandas as pd
import glob

data_folder = "Project\data\data/*.csv"
all_files=glob.glob(data_folder)
for file in all_files:
    df=pd.read_csv(file)
    df['price'] = df['price'].str.replace('$', '', regex=False).astype(float)
    ch=df[df['product'] == 'pink morsel']
    ch['sales']=ch['price']*ch['quantity']
    ch.drop(['price','quantity'],axis=1, inplace=True)
    ch=ch[['product','sales','date','region']]
    print(ch)
