from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

def func(x):
    return x**2

interact(func, x = 10)