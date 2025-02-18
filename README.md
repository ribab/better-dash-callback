# better-dash-callback

A library that enables running clientside callback functions in Dash applications using Python syntax, eliminating the need for inline JavaScript.

## Problem

When building Dash applications, you often need to write clientside callback functions using inline JavaScript. This can be cumbersome and error-prone, especially for complex logic. Moreover, inline JavaScript code lacks syntax highlighting and debugging capabilities.

## Solution

`better-dash-callback` provides a solution to this problem by allowing you to write clientside callback functions using Python syntax. This makes your code more readable, maintainable, and efficient.

## Example

Let's consider a simple example where we want to update the text of a component based on the value of an input component.

**Using Dash's `clientside_callback`**

```python
import dash
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Input(id="input", type="text"),
    html.Div(id="output")
])

app.clientside_callback(
    """
    function(value) {
        return 'You entered: ' + value;
    }
    """,
    Output("output", "children"),
    Input("input", "value")
)

if __name__ == "__main__":
    app.run_server(debug=True)
```

**Using `better-dash-callback`**

```python
import dash
from dash import html
from better_dash_callback import callback

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Input(id="input", type="text"),
    html.Div(id="output")
])

@callback(
    Output("output", "children"),
    Input("input", "value"),
    clientside=True,
    prevent_initial_call=True
)
def update_output(value):
    return f"You entered: {value}"

if __name__ == "__main__":
    app.run_server(debug=True)
```

As you can see, the `better-dash-callback` example is more elegant and easier to read. You can write your callback function using Python syntax, without having to worry about inline JavaScript code.

The `callback` function takes the following additional arguments:

* `clientside`: A boolean indicating whether the callback should be executed on the client-side (default is `False`).
* `enable_es6`: A boolean indicating whether to enable ES6 syntax in the generated JavaScript code (default is `True`).
* `enable_stage3`: A boolean indicating whether to enable Stage 3 syntax in the generated JavaScript code (default is `True`).
* `*args` and `**kwargs`: Any arguments and keyword-arguments supported by `dash.callback` are also supported by `better-dash-callback.callback`

## Installation

To install `better-dash-callback`, you can use `pip`:

```bash
pip3 install better-dash-callback
```

## License

`better-dash-callback` is licensed under the MIT License.
