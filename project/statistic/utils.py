import matplotlib.pyplot as plt
import plotly.graph_objs as go
from io import BytesIO
import base64

def plot():
    x = [1, 2, 3, 4, 5]
    y = [10, 8, 6, 4, 2]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines'))

    context = {'plot': fig.to_html(full_html=False)}

    return context