#imports
import numpy as np
import csv

#Read csv
file = open("trainingdata.csv")
filereader = csv.reader(file)
inputs = []
outputs = []
for row in filereader:
    inputs.append(row[0:len(row)])
    outputs.append(row[len(row)])
file.close()

#Define NeuralNet class
class NeuralNet:
    #Columns refers to the number of data points given for each entry
    def __init__(self, columns):
        #Assign random weights
        np.random.seed(1)
        #Initialize weight to a random value in the range -1 to 1
        self.weight = 2 * np.random.random((columns,1)) - 1 
    def __calc_output(self, data):
        #Calculate weighted sum
        weight_sum = np.dot(data, self.weight)
        #Sigmoid function normalizes result to lie between 0 and 1
        return 1 / (1 + np.exp(weight_sum * -1))
    def __train(self, train_output, train_input, iterations):
        
        
        
        
        
        
        