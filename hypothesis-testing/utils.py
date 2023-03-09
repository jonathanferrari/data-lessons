import numpy as np
from datascience import *
from ipywidgets import *
from IPython.display import *

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

def feedback_button() -> None:
    button = '''
    <style>
    .button {
        border: 0;
        padding: 16px 32px 16px 32px;
        text-align: center;
        font-size: 18px;
        display: flex;
        transition: color 5s, 
                    background 5s, 
                    box-shadow 1s ease-out;
        cursor: pointer;
        color: #003262;
        border-radius: 30px;
        margin: 10% auto;
        background: linear-gradient(145deg, #e2e2e2, #bebebe);
        box-shadow: 20px 20px 40px 10px #afafaf, 
                    -20px -20px 40px 10px #f7f7f7, 
                    inset 0 0 0px, 
                    inset 0 0 0px;
    }
    
    .button:hover {
        color: #D3D3D3;
        background: #003262;
        box-shadow: 0 0 0px #000000, 
                    0 0 0px #000000, 
                    inset 20px 20px 40px 10px #002a51, 
                    inset -20px -20px 40px 10px #003b73;
    }
    </style>
    <a href="https://forms.gle/hipxf2uFw5Ud4Hyn8">
        <button class="button">
            Fill out the feedback form here
        </button>
    </a>
    '''
    display(HTML(button))
