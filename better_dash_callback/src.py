#!/usr/bin/env python3
import metapensiero.pj.__main__
import dash
import inspect

def callback(*args, clientside=False, disable_es6=False, enable_stage3=False, **kwargs):
    """
    A decorator to register a Dash callback. If `clientside` is True, the python callback
    will be executed clientside using https://github.com/metapensiero/metapensiero.pj
    which will convert it to javascript.
    
    If `clientside` is False or not set, the callback will be executed serverside
    using Dash's standard callback system.

    Other than clientside argument, all other arguments are the same as Dash's @callback function.

    :param clientside: Whether to execute the callback clientside. Defaults to False.
    :param enable_es6: Whether to enable ES6 syntax. Defaults to True.
    :param enable_stage3: Whether to enable Stage3 syntax. Defaults to True.
    :param args: Arguments to pass to the Dash callback. Include dash.Output, dash.Input, and dash.State.
    :param kwargs: Keyword arguments to pass to the Dash callback. Includes `prevent_initial_call=True`.
    """
    
    def decorator(func):
            
        if clientside:
            python_code = inspect.getsource(func)
            python_code = python_code[python_code.find("def "):]
            js_code = metapensiero.pj.__main__.transform_string(python_code, enable_es6=not disable_es6, enable_stage3=enable_stage3)
            dash.clientside_callback(js_code, *args, **kwargs)
        else:
            @dash.callback(*args, **kwargs)
            def wrapper(*values):
                return func(*values)

    return decorator
