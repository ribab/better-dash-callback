import dash
from dash import html, dcc, Output, Input
from better_dash_callback import callback

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id="input", type="text"),
    html.Div(id="output")
])

@callback(
    Output("output", "children"),
    Input("input", "value"),
    clientside=True
)
def update_output(value):
    """
    this code will be executed clientside as javascript.
    This page shows what syntax is supported: https://github.com/metapensiero/metapensiero.pj
    """
    return f"You entered: {value}"

if __name__ == "__main__":
    app.run_server(debug=True)
