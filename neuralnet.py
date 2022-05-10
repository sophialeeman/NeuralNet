#imports
import numpy as np
import csv

#Read csv
file = open("trainingdata.csv")
filereader = csv.reader(file)
rows = []
for row in filereader:
    rows.append(row)
file.close()

#Define NeuralNet class
class NeuralNet:
    #Columns refers to the number of data points given for each entry
    def __init__(self, columns):
        #Assign random weights
        np.random.seed(1)
        #Initialize weight to a random value in the range -1 to 1
        self.weight = 2 * np.random.random((columns,1)) - 1 
    def __calc_output(self, traindata):
        #Calculate weighted sum
        weight_sum = np.dot(traindata, self.weight)
        #Sigmoid function normalizes result to lie between 0 and 1
        return 1 / (1 + np.exp(weight_sum * -1))
    
        
        
        
        
        
        