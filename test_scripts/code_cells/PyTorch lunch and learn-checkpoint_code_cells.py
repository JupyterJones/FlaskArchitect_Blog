

# imports
import torch
from torch import nn
from torch.optim import SGD
from torch.utils.data import DataLoader
from torch.autograd import Variable
from torchvision.datasets import MNIST
from torch.utils.data import DataLoader
from torchvision.transforms import ToTensor, Normalize, Compose
from IPython.display import Image
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

# summary of neural networks
Image(url='https://i.imgur.com/ktUOnca.jpg')

Image(url="http://www.frank-dieterle.de/phd/images/image016.gif")

# how tensors work
x = torch.zeros(2,3)
x

# how variables work
x = Variable(x)
print ("x:", x)
print ("requires grad:", x.requires_grad)
print ("data:", x.data)

y = x + 1
z = Variable(torch.ones(2,3), requires_grad=True)
w = y+z

print (y)
print ("does y require grad?", y.requires_grad)
print ("does w require grad?", w.requires_grad)

# what about neural network layers?
lin = nn.Linear(3, 4)  # 3 inputs and 4 outputs. Should contain a 4x3 matrix and a 4x1 matrix of parameters.
list(lin.parameters())

print ("lin output", lin(y))  # processing with a batch size of 2.
print (lin(y).requires_grad)
print (lin(w).requires_grad)

relu = nn.ReLU()
print (relu(lin(y)))
print (relu(lin(y)).requires_grad)
print (relu(w).requires_grad)
print (relu(y).requires_grad)

Image(url="https://i.stack.imgur.com/GvsBA.jpg")

Image(url="http://d3kbpzbmcynnmx.cloudfront.net/wp-content/uploads/2015/09/rnn.jpg")

# setting up datasets.
training = DataLoader(
    MNIST(
        "/home/jack/train", 
        download=False, 
        transform=Compose([ToTensor(),Normalize((0.1307,), (0.3081,))])
    ), 
    batch_size=64, 
    shuffle=True, 
    num_workers=40
)
testing = DataLoader(
    MNIST(
        "/home/jack/test", 
        train=False,
        download=False, 
        transform=Compose([ToTensor(),Normalize((0.1307,), (0.3081,))])
    ), 
    batch_size=64, 
    shuffle=True, 
    num_workers=40
)


len(training.dataset), len(testing.dataset)

print (MNIST('/home/jack/train')[0])
MNIST('/home/jack/train')[0][0]

# basic linear with relu's
class LinReLU(nn.Module):
    def __init__(self, indim, outdim):
        super(LinReLU, self).__init__()
        self.lin = nn.Linear(indim, outdim)
        self.relu = nn.ReLU(True)
    
    def forward(self, input):
        input = self.lin(input)
        return self.relu(input)


class MnistLinear(nn.Module):
    def __init__(self):
        super(MnistLinear, self).__init__()
        self.lin1 = LinReLU(28*28, 16)
        self.lin2 = nn.Linear(16, 10)
    
    def forward(self, input):
        input = self.lin1(input.view(-1, 28*28))
        input = self.lin2(input)
        return input

class ConvReLU(nn.Module):
    def __init__(self, in_channels, out_channels, kernel=3):
        super(ConvReLU, self).__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel, padding=kernel/2)
        self.relu = nn.ReLU(True)
        self.bn = nn.BatchNorm2d(out_channels)
    
    def forward(self, input):
        input = self.conv(input)
        input = self.relu(input)
        return self.bn(input)


class MnistCNN(nn.Module):
    def __init__(self):
        super(MnistCNN, self).__init__()
        self.conv1 = ConvReLU(1, 16)
        self.mp = nn.MaxPool2d(2)
        self.conv2 = ConvReLU(16, 32)
        self.avgpool = nn.AvgPool2d(14)
        self.lin = nn.Linear(32, 10)
    
    def forward(self, input):
        input = self.conv1(input)
        input = self.mp(input)
        input = self.conv2(input)
        input = self.avgpool(input).squeeze()
        return self.lin(input)

class MnistRNN(nn.Module):
    def __init__(self):
        super(MnistRNN, self).__init__()
        self.lstm = nn.LSTM(
            input_size=28, 
            hidden_size=16, 
            num_layers=2, 
            batch_first=True, 
            dropout=0.5
        )
        self.linear = nn.Linear(16, 10)
    
    def forward(self, input):
        input, hidden = self.lstm(input.squeeze())
        return self.linear(input[:, -1])

class ComboModel(nn.Module):
    def __init__(self):
        super(ComboModel, self).__init__()
        self.lin = MnistLinear()
        self.cnn = MnistCNN()
        self.rnn = MnistRNN()
    
    def forward(self, input):
        l1 = self.lin(input)
        l2 = self.cnn(input)
        l3 = self.rnn(input)
        return l1, l2, l3 

model = ComboModel()

def num_parameters(m):
    return sum([y.nelement() for y in m.parameters()])

print ("num params for linear:\t", num_parameters(model.lin))
print ("num params for cnn:\t", num_parameters(model.cnn))
print ("num params for rnn:\t", num_parameters(model.rnn))

optimizer = SGD(model.parameters(), lr=0.05, momentum=0.9)

model = model.cpu()

loss = nn.CrossEntropyLoss().cpu()

sav = open("SAV.Epoch","a")
def train(epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(training):
        data, target = data.cpu(), target.cpu()
        data, target = Variable(data), Variable(target)
        optimizer.zero_grad()
        lin_out, cnn_out, rnn_out = model(data)
        lin_loss = loss(lin_out, target)
        cnn_loss = loss(cnn_out, target)
        rnn_loss = loss(rnn_out, target)
        total_loss = lin_loss + cnn_loss + rnn_loss
        total_loss.backward()
        optimizer.step()
        if batch_idx % 100 == 0:
            txt= str('Train Epoch: {} [{}/{} ({:.0f}%)]\tLin Loss: {:.6f}\tCNN Loss: {:.6f}\tRNN Loss: {:.6f}'.format(
                epoch+1, batch_idx, len(training),
                100. * batch_idx / len(training), lin_loss.data[0], cnn_loss.data[0], rnn_loss.data[0]))
            sav.write(txt)
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLin Loss: {:.6f}\tCNN Loss: {:.6f}\tRNN Loss: {:.6f}'.format(
                epoch+1, batch_idx, len(training),
                100. * batch_idx / len(training), lin_loss.data[0], cnn_loss.data[0], rnn_loss.data[0]))

num_epochs = 10
losses = [{}] * (num_epochs+1)
correct = [{}] * (num_epochs+1)

def test(epoch):
    #with torch.no_grad():
    model.eval()
    losses[epoch] = dict(
        Linear=0,
        CNN=0,
        RNN=0
    )
    correct[epoch] = dict(
        Linear=0,
        CNN=0,
        RNN=0
    )
    for data, target in testing:
        with torch.no_grad():
            data, target = data.cpu(), target.cpu()
            data, target = Variable(data, volatile=False), Variable(target)
            data, target = Variable(data), Variable(target)
            lin_out, cnn_out, rnn_out = model(data)
        
        for name, output in [("Linear", lin_out), ("CNN", cnn_out), ("RNN", rnn_out)]:
            losses[epoch][name] += loss(output, target).data[0]
            pred = output.data.max(1)[1] 
            correct[epoch][name] += pred.eq(target.data).cpu().sum()

    for name in ['Linear', 'CNN', 'RNN']:
        losses[epoch][name] /= len(testing) # loss function already averages over batch size
        print('{} Test set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
            name, losses[epoch][name], correct[epoch][name], len(testing.dataset),
            100. * correct[epoch][name] / len(testing.dataset)))
        tex2=str('{} Test set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
            name, losses[epoch][name], correct[epoch][name], len(testing.dataset),
            100. * correct[epoch][name] / len(testing.dataset)))
        sav.write(txt2)
        
for epoch in range(num_epochs+1):
    test(epoch)
    train(epoch)
test(num_epochs)

scatters = []
for name in ['Linear', 'CNN', 'RNN']:
    xs = [i for i in range(1, num_epochs+1)]
    ys = [float(i[name])/len(testing.dataset) for i in correct]
    scatters.append(go.Scatter(
        x = xs,
        y = ys,
        name=name
    ))
    print ys
iplot(scatters)



