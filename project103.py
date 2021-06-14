import pandas as pd
import plotly.express as px

pf=pd.read_csv("project103data1.csv")
fig=px.scatter(pf,x='date',y='cases',color=("country"))
fig.show()