import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

########### Set up the chart
year = np.linspace(2013, 1, 2017)

pubcov_blk = np.array([40.7,42.3,43.5,44.0,43.7])
pubcov_non = np.array([30.3,31.9,33.5,34.2,34.3])
pubcov_tot = np.array([31.7,33.3,34.9,35.6,35.6])

prvcov_blk = np.array([49.7,51.7,53.5,54.6,54.5])
prvcov_non = np.array([67.0,68.2,69.2,69.4,69.2])
prvcov_tot = np.array([64.6,65.9,67.0,67.3,67.2])

anycov_blk = np.array([82.4,85.8,88.4,89.7,89.4])
anycov_non = np.array([85.7,88.4,90.6,91.4,91.2])
anycov_tot = np.array([85.2,88.0,90.3,91.1,91.0])

# Create traces
trace_any_tot = go.Scatter(
  x = year,
  y = anycov_tot,
  mode = 'lines+markers',
  name = 'Any (All)',
  line = dict(
    color = ('rgb(0, 0, 0)'),
    width = 2,)
)
trace_any_blk = go.Scatter(
  x = year,
  y = anycov_blk,
  mode = 'lines+markers',
  name = 'Any (Black)',
  line = dict(
    color = ('rgb(0, 0, 0)'),
    width = 2,
    dash = 'dashdot')
)
trace_any_non = go.Scatter(
  x = year,
  y = anycov_non,
  mode = 'lines+markers',
  name = 'Any (Non-Black)',
  line = dict(
    color = ('rgb(0, 0, 0)'),
    width = 2,
    dash = 'dash')
)

trace_prv_tot = go.Scatter(
  x = year,
  y = prvcov_tot,
  mode = 'lines+markers',
  name = 'Private (All)',
  line = dict(
    color = ('rgb(22, 96, 167)'),
    width = 2,)
)
trace_prv_blk = go.Scatter(
  x = year,
  y = prvcov_blk,
  mode = 'lines+markers',
  name = 'Private (Black)',
  line = dict(
    color = ('rgb(22, 96, 167)'),
    width = 2,
    dash = 'dashdot')
)
trace_prv_non = go.Scatter(
  x = year,
  y = prvcov_non,
  mode = 'lines+markers',
  name = 'Private (Non-Black)',
  line = dict(
    color = ('rgb(22, 96, 167)'),
    width = 2,
    dash = 'dash')
)

trace_pub_tot = go.Scatter(
  x = year,
  y = pubcov_tot,
  mode = 'lines+markers',
  name = 'Public (All)',
  line = dict(
    color = ('rgb(205, 12, 24)'),
    width = 2,)
)
trace_pub_blk = go.Scatter(
  x = year,
  y = pubcov_blk,
  mode = 'lines+markers',
  name = 'Public (Black)',
  line = dict(
    color = ('rgb(205, 12, 24)'),
    width = 2,
    dash = 'dashdot')
)
trace_pub_non = go.Scatter(
  x = year,
  y = pubcov_non,
  mode = 'lines+markers',
  name = 'Public (Non-Black)',
  line = dict(
    color = ('rgb(205, 12, 24)'),
    width = 2,
    dash = 'dash')
)

census_data = [trace_any_tot, trace_any_blk, trace_any_non,
               trace_prv_tot, trace_prv_blk, trace_prv_non,
               trace_pub_tot, trace_pub_blk, trace_pub_non]

# Edit layout
census_layout = dict(title = 'Disparity in Health Insurance Coverage by Race',
                     xaxis = dict(title = 'Year',
                                  dtick = 1,
                                  autorange = True),
                     yaxis = dict(title = 'Insured (% National Population)',
                                  dtick = 10,
                                  range = [0,100])
                     )

census_fig = go.Figure(data=census_data, layout=census_layout)

########### Display the chart

app = dash.Dash()
server = app.server

app.layout = html.Div(children=[
    html.H1('Health Insurance Coverage Disparity'),
    dcc.Graph(
        id='census',
        figure=census_fig
    ),
    html.A('Code on Github', href='https://github.com/stauntonjr/DTI_2019_Project_Proposal'),
    html.Br(),
    html.A('Data Source', href='https://www.census.gov/programs-surveys/acs/data/pums.html'),
    ]
)

if __name__ == '__main__':
    app.run_server()
