import matplotlib.pyplot as plt
import plotly.graph_objs as go
from io import BytesIO
import numpy as np
import base64

def plot(data):
    x = [float(q) for q in range(5,101,5)]
    pr_dict= {key:0 for key in x}

    for item in data:
        pr_dict[item.pass_rate]+=1
    

    y = [value for _,value in pr_dict.items()]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=x, y=y))
    fig.update_xaxes(type='category')
    fig.update_layout(
        
        title="Challenge Barplot",
        xaxis_title="Pass rate (%)",
        yaxis_title="Counts",)

    context = {'plot': fig.to_html(full_html=False)}

    return context