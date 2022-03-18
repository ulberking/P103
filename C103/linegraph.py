import pandas as pd
import plotly.express as px
df = pd.read_csv('C:/Users/Minho/OneDrive/바탕 화면/python/C103/csv files/line_chart.csv')
graph = px.line(df,x='Year',y='Per capita income',color='Country')
graph.show()