import ipywidgets
label = ipywidgets.Label('Hello World')
label

# it should also handle custom msg'es
label.send({'msg': 'Hello'})

