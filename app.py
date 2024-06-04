# Import relevant libraries
import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State

 # Load dataset
data = pd.read_csv('data/titanic.csv')
pie_fig = px.pie(df, names='Sex',facet_col="Pclass",title="percentage of Gender per each pclass")
pie_fig .update_layout(plot_bgcolor='white')
scatter_fig=px.scatter(df,x='Age', y='Fare',color='Survived', size="Pclass",size_max=20,title="Scatter Plot far vs. age")
scatter_fig.update_layout(plot_bgcolor='white')
NewDF2=df[[ "SibSp"]].value_counts().reset_index(name='count').sort_values(by='SibSp')
bar_fig=px.bar(NewDF2,x="SibSp",y="count" ,title='sum of sibling-spouses')
bar_fig.update_layout(plot_bgcolor='white')
histogram_fig=px.histogram(df,x="Parch",title='sum of parent-child')
histogram_fig.update_layout(plot_bgcolor='white')
NewDF1=df[[ "Parch"]].value_counts().reset_index(name='count')
line_fig=px.line(NewDF1,x="Parch",y="count",markers="Parch",title='sum of parent-child' )
line_fig.update_layout(plot_bgcolor='white')


# Create the Dash app
app = dash.Dash(__name__)
server = app.server

# Define the layout of the dashboard
app.layout = html.Div([
        html.H1("DashBoard using plotly", style={'textAlign':'center','background':'DarkCyan','fontSize':80}),
        ####################################
        html.H1("PIE GRAPH", style={'textAlign':'center','background':'LightBlue','fontSize':50} ),
        dcc.Graph(figure=pie_fig),

        html.H1("SCATTER GRAPH", style={'textAlign':'center','background':'LightBlue','fontSize':50} ),
        dcc.Graph(figure=scatter_fig),
    
        html.H1("BAR GRAPH", style={'textAlign':'center','background':'LightBlue','fontSize':50}),
        dcc.Graph(figure=bar_fig),

        html.H1("HISTOGRAM GRAPH", style={'textAlign':'center','background':'LightBlue','fontSize':50} ),
        dcc.Graph(figure=histogram_fig),
        
        html.H1("LINE GRAPH", style={'textAlign':'center','background':'LightBlue','fontSize':50}),
        dcc.Graph(figure=line_fig)
])

if __name__ == '__main__':
    app.run_server(debug=False)
