from ipykernel.comm import Comm

comm = Comm('this-comm-tests-a-missing-handler', data={'id': 'foo'})

comm.send(data={'id': 'bar'})

