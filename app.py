import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

# coverage chart data
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
trace_pub_blk = go.Scatter(
  x = year,
  y = pubcov_blk
  mode = 'lines+markers'
  name = 'Black (public)'
  line = dict(
    color = ('rgb(205, 12, 24)'),
    width = 4,
    dash = 'dashdot')
)
trace_pub_non = go.Scatter(
  x = year,
  y = pubcov_non
  mode = 'lines+markers'
  name = 'Non-Black (public)'
  line = dict(
    color = ('rgb(205, 12, 24)'),
    width = 4,
    dash = 'dash')
)
trace_pub_tot = go.Scatter(
  x = year,
  y = pubcov_tot
  mode = 'lines+markers'
  name = 'All (public)'
  line = dict(
    color = ('rgb(205, 12, 24)'),
    width = 4,)
)

trace_prv_blk = go.Scatter(
  x = year,
  y = prvcov_blk
  mode = 'lines+markers'
  name = 'Black (private)'
  line = dict(
    color = ('rgb(22, 96, 167)'),
    width = 4,
    dash = 'dashdot')
)
trace_prv_non = go.Scatter(
  x = year,
  y = prvcov_non
  mode = 'lines+markers'
  name = 'Non-Black (private)'
  line = dict(
    color = ('rgb(22, 96, 167)'),
    width = 4,
    dash = 'dash')
)
trace_prv_tot = go.Scatter(
  x = year,
  y = prvcov_tot
  mode = 'lines+markers'
  name = 'All (private)'
  line = dict(
    color = ('rgb(22, 96, 167)'),
    width = 4,)
)

trace_any_blk = go.Scatter(
  x = year,
  y = anycov_blk
  mode = 'lines+markers'
  name = 'Black (any)'
  line = dict(
    color = ('rgb(0, 0, 0)'),
    width = 4,
    dash = 'dashdot')
)
trace_any_non = go.Scatter(
  x = year,
  y = anycov_non
  mode = 'lines+markers'
  name = 'Non-Black (any)'
  line = dict(
    color = ('rgb(0, 0, 0)'),
    width = 4,
    dash = 'dash')
)
trace_any_tot = go.Scatter(
  x = year,
  y = anycov_tot
  mode = 'lines+markers'
  name = 'All (any)'
  line = dict(
    color = ('rgb(0, 0, 0)'),
    width = 4,)
)
data = [trace_pub_blk, trace_pub_non, trace_pub_tot, 
            trace_prv_blk, trace_prv_non, trace_prv_tot,
            trace_any_blk, trace_any_non, trace_any_tot]

# Edit layout
layout = dict(title = 'Disparity in Health Insurance Coverage by Race',
              xaxis = dict(title = 'Year'),
              yaxis = dict(title = 'Insured (% National Population)'),
              )
              
fig = dict(data=data, layout=layout)
py.iplot(fig, filename='coverage')

