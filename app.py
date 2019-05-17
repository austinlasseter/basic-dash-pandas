######### Import your libraries #######
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import *


####### Set up your app #####
app = dash.Dash(__name__)
server = app.server
app.title='Titanic!'
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

###### Import a dataframe #######
df = pd.read_csv("https://raw.githubusercontent.com/austinlasseter/plotly_dash_tutorial/master/00%20resources/titanic.csv")

var_list=['Age', 'Fare', 'Survived', 'Pclass']




####### Layout of the app ########
app.layout = html.Div([
    html.H3('Choose a color from the list:'),
    dcc.Dropdown(
        id='my-dropdown-input',
        options=[{'label': i, 'value': i} for i in colors_list],
        value=var_list[0]
    ),
    html.Br(),
    dcc.Graph(id='my-output-window')
])


######### Interactive callbacks go here #########
@app.callback(dash.dependencies.Output('my-output-window', 'figure'),
              [dash.dependencies.Input('my-dropdown-input', 'value')])
def display_value(user_input):
    results = df.groupby('Embarked')[user_input].mean()
    mydata = [go.Bar(x = results.index,
                     y = results.values,
                     marker = dict(color='lightblue'))]
    mylayout = go.Layout(title = 'This is a cool bar chart',
                         xaxis = dict(title='this is my x-axis'),
                         yaxis = dict(title='this is my y-axis'))
    myfig = go.Figure(data=mydata, layout=mylayout)
    return myfig


######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
