import numpy as np
from datascience import *
from ipywidgets import *

pairs = [("TVD", lambda left, right: abs(left - right)/2), 
         ("Absolute Difference", lambda left, right: abs(left - right)),
         ("Distance from Expected of Left Hands", lambda left, right: abs(left - 20)),
         ("Distance from Expected of Right Hands", lambda left, right: abs(right - 20)),
         ("Proportion", lambda left, right: max([left, right])/min([left, right])),
         ("Total Distance from Expected", lambda left, right: abs(right - 20) + abs(left - 20)),
         ("Left Minus Right", lambda left, right: left - right),
         ("Right Minus Left", lambda left, right: right - left)]

def all_ints(arr):
    for i in arr:
        if i != i//1:
            return False
    return True
  
def show_general(*args, tags: list = [], map: dict = None) -> None:
    """Pretty Display"""
    assert (tags == []) or (isinstance(tags[0], str)
                            ), "tags must contain strings"
    if map:
        for s, tags in map.items():
            show(s, tags=tags)
        return
    for i in args:
        if type(i) != str:
            i = str(i)
        for tag in tags:
            i = f"<{tag}>{i}</{tag}>"
        display(Markdown(i))

def show(*args, n = 20):
    show_general("")
    for arg in args:
        show_general(arg, tags=[f"p style='font-size:{n}px'"])
        
def add_observed(fig, x, text = "Observed Value", style = "solid", width = 3, color = "#E2C258"):
    return fig.add_vline(x = x, annotation_text = text,
                         line_dash = style, line_color = color, line_width = width)
