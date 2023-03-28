import matplotlib.pyplot as plt
import pandas as pd
from django.http import HttpResponse
import seaborn as sns
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from io import BytesIO

import base64

def plot():
    x = [1, 2, 3, 4, 5]
    y = [10, 8, 6, 4, 2]
    fig = plt.figure()
    plt.plot(x, y)

    buf = BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8').replace('\n', '')

    return image_base64