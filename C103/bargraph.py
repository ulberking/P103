import pandas as pd
import plotly.express as px
df = pd.read_csv('C:/Users/Minho/OneDrive/바탕 화면/python/C103/csv files/data.csv')
graph=px.bar(df,x='Country',y='Population')
graph.show()