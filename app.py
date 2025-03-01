
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import glob

app = Dash()

data="Project\data\data/*.csv"
all_files =glob.glob(data)

dh={}
for file in all_files:
    df=pd.read_csv(file)
    df['price'] = df['price'].str.replace('$', '', regex=False).astype(float)
    ch=df[df['product'] == 'pink morsel']
    ch['sales']=ch['price']*ch['quantity']
    ch['date']=ch['date']>='2021-01-15'
    ch.drop(['price','quantity'],axis=1, inplace=True)
  
    dh=pd.DataFrame(ch)

fig = px.bar(dh, x="date", y="sales", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
             
         FALSE="After the price increase"
         True="Before the price increse"
    '''),

    dcc.Graph(
        id='graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)

