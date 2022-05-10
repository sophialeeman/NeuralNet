import csv
import numpy as np
from neuralnet import NeuralNet

#Read csv
file = open("trainingdata.csv")
filereader = csv.reader(file)
inputs = []
outputs = []
for row in filereader:
    inputs.append(row[0:len(row)-1])
    outputs.append([row[len(row)-1]])
file.close()

inputs = np.array(inputs).astype(float)
outputs = np.array(outputs).astype(float)
neural_network = NeuralNet(3)
neural_network.train(outputs, inputs, 10000)
print(neural_network.calc_output([1,0,0]))
