# Chapter **16.**  Introduction to GUIs

## Introduction to GUIs
* __interact() :__

```python

# Import package
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

# Very basic function
def f(x):
    return x

# Int generate slider
interact(f, x=10,);
interact(f, x=widgets.IntSlider(min=-10,max=30,step=1,value=10));
# Add ";" to remove output "<function __main__.f>"
# x=10: The initial value of the slider

# Booleans generate check-boxes
interact(f, x=True);

# Strings generate text areas
interact(f, x='Hi there!');

# List generate drop-down menu
interact(f, x=['apples','oranges']);

# Dict generate drop-down menu with values
interact(f, x={'one': 10, 'two': 20});

# Using a decorator!
@interact(x=True, y=1.0)
def g(x, y):
    return (x, y)

# Fixed value in interact
interact(g, x=True, y=fixed(1.0));

# Float slider (Simply just add decimal point)
interact(f, x=10.0,);

# Slider abbreviation (max,min,step)
# (min, max, step)
interact(f, x=(0,8,2));          # Int   slider
interact(f, x=(0.0,10.0,0.01));  # float slider

# Slider abbreviation with decorator
@interact(x=(0.0,20.0,0.5))
def h(x=5.5):
    return x
```

* __interactive() :__  
Unlike interact, the return value of the function will not be displayed automatically
```python
# Import module
from IPython.display import display

def f(a, b):
    display(a + b)
    return a+b

# Return an widget object 
w = interactive(f, a=10, b=20)

# Check params status
w.children
# > (IntSlider(value=10, description='a', max=30, min=-10),
# >  IntSlider(value=20, description='b', max=60, min=-20),
# >  Output())

# Display GUI
display(w)

# Show function input values
w.kwargs
# > {'a': 3, 'b': 20}

# Show function return value 
w.result
# > 23
```

## Widget Basic
```python

# Import module ipywidgets & IPython
import ipywidgets as widgets
from IPython.display import display

# Construct, display and close widget
w = widgets.IntSlider()
display(w)
w.close()

# Widget properties
w.value  # function return value
w.keys   # Show all the params in widget object!
# > ['max',
# >  'min',
# >  'orientation',
# >  'readout',
# >  'readout_format',
# >  'step',
# >  'style',
# >  'value'...]

# Sync two similar widgets
a = widgets.FloatText()
b = widgets.FloatSlider()
display(a,b)

mylink = widgets.jslink((a, 'value'), (b, 'value'))

# Unlink two widgets
mylink.unlink()
```

## Checkout jupyter notebook for more details
* [__Widget list    :__][0] Show all basic widgets available in __ipywidgets__
* [__Widget Styling :__][1] Show various ways to style widgets. __style()__ and __layout()__
* [__Widget Events  :__][2] Button clicks
* [__Widget Example :__][3] Lorenz system of differential equations
* [__Advanced Widget:__][4] More advance widgets

[0]: https://github.com/alonzo3569/python/blob/master/16-Bonus%20Material%20-%20Introduction%20to%20GUIs/03-Widget%20List.ipynb
[1]: https://github.com/alonzo3569/python/blob/master/16-Bonus%20Material%20-%20Introduction%20to%20GUIs/05-Widget%20Styling.ipynb
[2]: https://github.com/alonzo3569/python/blob/master/16-Bonus%20Material%20-%20Introduction%20to%20GUIs/04-Widget%20Events.ipynb
[3]: https://github.com/alonzo3569/python/blob/master/16-Bonus%20Material%20-%20Introduction%20to%20GUIs/06-Custom%20Widget.ipynb
[4]: https://github.com/alonzo3569/python/blob/master/16-Bonus%20Material%20-%20Introduction%20to%20GUIs/07-Advanced%20Widget%20List.ipynb
