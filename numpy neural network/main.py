import numpy 
import matplotlib.pyplot as plot

# Training data set
# Each of these letters is represented in 1s and 0s (shapewise).

tree =[0, 0, 0, 1, 1, 0, 0, 0, 
    0, 0, 1, 1, 1, 1, 0, 0,
    0, 0, 0, 1, 1, 0, 0, 0, 
    0, 1, 1, 1, 1, 1, 1, 0,
    0, 0, 1, 1, 1, 1, 0, 0,
    1, 1, 1, 1, 1, 1, 1, 1,
    0, 1, 1, 1, 1, 1, 1, 0,
    1, 1, 1, 1, 1, 1, 1, 1] 

b =[0, 1, 1, 1, 1, 0, 0, 0, 
    0, 1, 0, 0, 0, 1, 0, 0,
    0, 1, 0, 0, 0, 1, 0, 0, 
    0, 1, 0, 0, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 0, 0, 0,
    0, 1, 0, 0, 0, 1, 0, 0,
    0, 1, 0, 0, 0, 1, 0, 0,
    0, 1, 1, 1, 1, 0, 0, 0] 

c =[0, 0, 1, 1, 1, 1, 0, 0, 
    0, 1, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 
    0, 1, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 0,
    0, 0, 1, 1, 1, 1, 0, 0] 

label = [[1,0,0], [0,1,0], [0,0,1]]

"""

Neural Network portion

def sigmoid: 
    - returns the logistics function which maps any real value to the range (0, 1)

def feedforward: 
    - hidden layers feed the input through different nodes

def generate weights:
    - initialises the weights randomly so that the back propagation function can adjust them

def loss:
    - uses the mean squared deviation function to find the performance 

def back propagation: 
    - trains our model by adjusting our parameters(weights and biases) through each feed forward pass

def training: 
    - takes all of our losses, and uses the other functions to generate the adjusted weights

def think:
    - takes input and returns the predicted answer

"""

# Converts the training set and labels into a numpy array

x = [   
        numpy.array(tree).reshape(1,64),
        numpy.array(b).reshape(1,64),
        numpy.array(c).reshape(1,64),
    ]

y = numpy.array(label)

# Main functions for our simple neural network
def sigmoid(x):
    return(1/(1 + numpy.exp(-x)))

def feedforward(x, w1, w2):
    z1 = x.dot(w1)
    a1 = sigmoid(z1)

    z2 = a1.dot(w2)
    a2 = sigmoid(z2)
    
    return(a2)

def generate_weights(x, y):
    l = []
    
    for i in range(x * y):
        l.append(numpy.random.randn())
    
    return(numpy.array(l).reshape(x, y))

def loss(out, Y):
    s = (numpy.square(out-Y))
    s = numpy.sum(s)/len(y)
    
    return(s)

def backpropagation(x, y, w1, w2, alpha):
    z1 = x.dot(w1)
    a1 = sigmoid(z1)

    z2 = a1.dot(w2)
    a2 = sigmoid(z2)

    d2 = (a2-y)
    d1 = numpy.multiply((w2.dot((d2.transpose()))).transpose(), (numpy.multiply(a1, 1-a1)))

    w1_adjusted = x.transpose().dot(d1)
    w2_adjusted = a1.transpose().dot(d2)

    w1 = w1-(alpha*(w1_adjusted))
    w2 = w2-(alpha*(w2_adjusted))

    return(w1, w2)

def training(x, Y, w1, w2, alpha = 0.01, epoch = 10):
    accuracy = []
    losses = []
    for i in range(epoch):
        l = []
        for j in range(len(x)):
            output = feedforward(x[j], w1, w2)
            l.append((loss(output, Y[j])))
            w1, w2 = backpropagation(x[j], y[j], w1, w2, alpha)
        print("iterations:", i+1, "     accuracy:", (1-(sum(l)/len(x)))*100)
        accuracy.append((1-(sum(l)/len(x)))*100)
        losses.append(sum(l)/len(x))
    
    return (accuracy, losses, w1, w2)

def think(x, w1, w2):
    out = feedforward(x, w1, w2)
    maximum = 0
    k = 0
    for i in range(len(out[0])):
        if (maximum<out[0][i]):
            maximum = out[0][i]
            k = i
    if (k==0):
        print("data set is a christmas tree!")
        plot.imshow(numpy.array(tree).reshape(8, 8))
        plot.show()
    elif(k==1):
        print("data set is a letter B")
        plot.imshow(numpy.array(b).reshape(8, 8))
        plot.show()
    else:
        print("data set is a letter C")
        plot.imshow(numpy.array(c).reshape(8, 8))
        plot.show()


# Generates the weights
# Prints the untrained weights

w1 = generate_weights(64, 8)
w2 = generate_weights(8, 3)

print("Untrained weights 1 :", w1)
print("Untrained weights 2 :", w2)

accuracy, losses, w1, w2 = training(x, y, w1, w2, 0.1, 100)

# Generates the trained weights
# Prints out the trained weights
print("Trained weights 1: ", w1)
print("Trained weights 2: ", w2)

"""
The think function takes in these arguments:
- 1, 0 image representation of the letter 
- w1 trained weights
- w2 trained weights
"""

think(x[0], w1, w2)




plot.plot(accuracy) 
plot.ylabel('Accuracy') 
plot.xlabel("Iterations:") 
plot.show() 

plot.plot(losses) 
plot.ylabel('Loss') 
plot.xlabel("Iterations:") 
plot.show()
