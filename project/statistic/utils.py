import plotly.graph_objs as go


def plot_challenge(data):
    x = [float(q) for q in range(5, 101, 5)]
    pr_dict = {key: 0 for key in x}

    for item in data:
        pr_dict[item.pass_rate] += 1

    y = [value for _, value in pr_dict.items()]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=x, y=y, text=y, textposition='outside',))
    fig.update_xaxes(type='category')
    fig.update_layout(
        title="Challenge Barplot",
        xaxis_title="Pass rate (%)",
        yaxis_title="Counts",)

    context = {'plot': fig.to_html(full_html=False)}

    return context


def plot_experiment(data):
    x = [float(q) for q in range(0, 101, 10)]
    pr_dict = {key: [0, 0, 0] for key in x}
    for item in data:
        if item.duration == 7000:
            pr_dict[item.pass_rate][0] += 1
        elif item.duration == 5000:
            pr_dict[item.pass_rate][1] += 1
        else:
            pr_dict[item.pass_rate][2] += 1
    easy, med, hard = [], [], []
    for _, v in pr_dict.items():
        easy.append(v[0])
        med.append(v[1])
        hard.append(v[2])
    fig = go.Figure(data=[
        go.Bar(name='Easy', x=x, y=easy, text=easy,  textposition='outside',),
        go.Bar(name='Medium', x=x, y=med, text=med,  textposition='outside',),
        go.Bar(name='Hard', x=x, y=hard, text=hard,  textposition='outside', ),
        ])
    fig.update_xaxes(type='category')
    fig.update_layout(
        title="Experiment Barplot",
        xaxis_title="Pass rate (%)",
        yaxis_title="Counts",)
    return fig.to_html(full_html=False)


def plot_pie_chart(exp, chal):
    easy, med, hard = 0, 0, 0
    for item in exp:
        if item.duration == 7000:
            easy += 1
        elif item.duration == 5000:
            med += 1
        else:
            hard += 1
    fig = go.Figure()
    fig.add_trace(go.Pie(values=[len(chal), easy, med, hard], labels=['Challenge', 'Easy', 'Medium', 'Hard']))
    fig.update_layout(
        title="Total counts PieChart")
    return fig.to_html(full_html=False)
