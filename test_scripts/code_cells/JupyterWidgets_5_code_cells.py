import ipywidgets
label = ipywidgets.Label('Hello World')
display(label)

# it should also handle custom msg'es
label.send({'msg': 'Hello'})

