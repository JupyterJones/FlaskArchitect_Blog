!jt -l


import IPython

bundle = {}
bundle['application/vnd.raw.v1+json'] = {
    'apples': ['🍎', '🍏'],
    'bananas': 2,
    'oranges': 'apples'
}

IPython.display.display(bundle, raw=True)



