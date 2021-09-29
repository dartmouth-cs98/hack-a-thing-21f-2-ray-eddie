#From https://plotly.com/python/
#and https://towardsdatascience.com/how-to-create-a-plotly-visualization-and-embed-it-on-websites-517c1a78568b
# Used https://blog.finxter.com/your-first-dash-app-how-to-get-started-in-4-minutes-or-less/ to use dashly to display fig rather than just using fig.show()
import plotly.express as px
import plotly.io as pio
from get_data import get_time_series, get_portfolio_value
import pandas as pd

import dash
from dash import dcc
from dash import html

es = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=es)

def generate_chart(portfolio, dates):
    dates = dates.dropna()
    string_dates = list(dates.index.strftime('%Y-%m-%d'))

    portfolio_values = pd.DataFrame(get_portfolio_value(portfolio, string_dates)).dropna()
    portfolio_values['date'] = portfolio_values.index
    fig = px.line(portfolio_values, x='date', y=portfolio_values.columns,
                hover_data={'date': "|%B %d, %Y"},
                title='Stock Price and Portfolio Value')
    fig.update_xaxes(
        dtick="M1",
        tickformat="%b\n%Y",
        ticklabelmode="period")
    app.layout = html.Div(children=[dcc.Graph(figure=fig)])

dates = pd.date_range(start='2020-01-01', end='2020-12-30', freq='D').to_series().dt.dayofweek.where(lambda x : x < 5)
portfolio = {'MSFT': 0.5, 'AAPL': 0.5}
generate_chart(portfolio, dates)

if __name__ == '__main__':
    app.run_server(debug=True)