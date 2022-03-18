import pandas as pd
import plotly.express as px
df=pd.read_csv('C:/Users/Minho/OneDrive/바탕 화면/python/C103/csv files/case.csv')
graph=px.scatter(df,x='date',y='cases',color='country')
graph.show()