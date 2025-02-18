#!/usr/bin/env python3
import metapensiero.pj.__main__
import dash
import inspect

def callback(*args, clientside=False, **kwargs):
    """
    A decorator to register a Dash callback. If `clientside` is True, the python callback
    will be executed clientside using jsbuilder, which will convert it to javascript.
    
    If `clientside` is False or not set, the callback will be executed serverside
    using Dash's standard callback system.

    Other than clientside argument, all other arguments are the same as Dash's @callback function.

    :param clientside: Whether to execute the callback clientside. Defaults to False.
    """
    
    def decorator(func):
            
        if clientside:
            python_code = inspect.getsource(func)
            python_code = python_code[python_code.find("def "):]
            js_code = metapensiero.pj.__main__.transform_string(python_code)
            dash.clientside_callback(js_code, *args, **kwargs)
        else:
            @dash.callback(*args, **kwargs)
            def wrapper(*values):
                return func(*values)

    return decorator
