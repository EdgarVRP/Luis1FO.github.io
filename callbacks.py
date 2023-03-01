# -*- coding: utf-8 -*-
# import dash IO and graph objects
from dash.dependencies import Input, Output
# Import dash html, bootstrap components, and tables for datatables
from dash import html
# Import app
from app import app
# Import custom data.py
import data
## Import data from data.py file
data_plan = data.plandata
data_cod=data.coddata
data_cons=data.consdata
data_pru=data.prudata
lan_data=data.landata
dsp_data=data.dspdata
op_data=data.opdata
mon_data=data.mondata

@app.callback_context(Output('output','children'),
              [Input('table', 'cols'),
               Input('table', 'rows'),
               Input('table', 'rowOrder'),
               Input('table', 'colOrder'),
               Input('table', 'aggregatorName'),
               Input('table', 'rendererName')],
               prevent_initial_call=True
              )
def display_props(cols, rows, row_order, col_order, aggregator, renderer):
    return [
        html.P(str(cols), id='columns'),
        html.P(str(rows), id='rows'),
        html.P(str(row_order), id='row_order'),
        html.P(str(col_order), id='col_order'),
        html.P(str(aggregator), id='aggregator'),
        html.P(str(renderer), id='renderer'),
    ]



