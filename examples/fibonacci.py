#!/usr/bin/env python3
from dash import Dash, html, dcc, Output, Input, State
from better_dash_callback import callback
    
@callback(
    Output("fibonacci_display", "children"),
    Output("fibonacci_values", "data"),
    Input("button", "n_clicks"),
    State("fibonacci_values", "data"),
    prevent_initial_call=True,
    clientside=True
)
def compute_next_fibonacci(_, values):
    """
    this code will be executed clientside as javascript.
    This page shows what syntax is supported: https://github.com/metapensiero/metapensiero.pj
    """
    ind = 0
    indices = []
    while ind < len(values) + 1:
        indices.push(ind)
        ind += 1
    if not values:
        values = [1]
    elif len(values) < 2:
        values.push(1)
    else:
        values.push(values[-1] + values[-2])
    result = ""
    for i in indices:
        if i > 0:
            result += " " + str(values[i])
        else:
            result += str(values[i])
    return result, values

app = Dash(__name__)
app.layout = [
    html.Button("Compute Fibonacci", id="button"),
    html.Span("1", id="fibonacci_display", style={"marginLeft": "10px"}),
    dcc.Store(id="fibonacci_values", data=[1]),
]

if __name__ == "__main__":
    app.run_server(debug=True)
