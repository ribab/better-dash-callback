# better-dash-callback

A library that enables running clientside callback functions in Dash applications using Python syntax, eliminating the need for inline JavaScript.

## Problem

When building Dash applications, you often need to write clientside callback functions using inline JavaScript. This can be cumbersome and error-prone, especially for complex logic. Moreover, inline JavaScript code lacks syntax highlighting and debugging capabilities.

## Solution

`better-dash-callback` provides a solution to this problem by allowing you to write clientside callback functions using Python syntax. This makes your code more readable, maintainable, and efficient.

## Dependencies

`better-dash-callback` depends on `metapensiero.pj`, a Python-to-JavaScript compiler that allows you to write Python code that can be executed in a JavaScript environment.

## Supported Python-to-JavaScript Syntax

The supported Python-to-JavaScript syntax is listed in the [metapensiero.pj documentation](https://github.com/metapensiero/metapensiero.pj). This includes support for many Python features, such as functions, classes, loops, and conditional statements.

## Example

Let's consider a simple example where we want to update the text of a component based on the value of an input component.

**Using Dash's `clientside_callback`**

```python
from dash import clientside_callback

clientside_callback(
    """
    function(value) {
        return 'You entered: ' + value;
    }
    """,
    Output("output", "children"),
    Input("input", "value")
)
```

**Using `better-dash-callback`**

```python
from better_dash_callback import callback

@callback(
    Output("output", "children"),
    Input("input", "value"),
    clientside=True
)
def update_output(value):
    return f"You entered: {value}"
```

As you can see, the `better-dash-callback` example is more elegant and easier to read. You can write your callback function using Python syntax, without having to worry about inline JavaScript code, and the code you write also includes all the python syntax highlighting rather than being javascript code inside of a python string.

The `callback` function takes the following additional arguments:

* `clientside`: A boolean indicating whether the callback should be executed on the client-side (default is `False`).
* `disable_es6`: A boolean indicating whether to disable ES6 syntax in the generated JavaScript code and revert back to ES5 support (default is `False`).
* `enable_stage3`: A boolean indicating whether to enable Stage 3 syntax in the generated JavaScript code (default is `False`).
* Any arguments and keyword-arguments supported by `dash.callback` are also supported by `better-dash-callback.callback`

## Installation

To install `better-dash-callback`, you can use `pip`:

```bash
pip3 install better-dash-callback
```

## License

`better-dash-callback` is licensed under the MIT License.
