#imports
import numpy as np

#Define NeuralNet class
class NeuralNet:
    #Columns refers to the number of data points given for each entry
    def __init__(self, columns):
        #Assign random weights
        np.random.seed(1)
        #Initialize weight to a random value in the range -1 to 1
        self.weight = 2 * np.random.random((columns,1)) - 1 
    def calc_output(self, data):
        #Calculate weighted sum
        weight_sum = np.dot(data, self.weight)
        #Sigmoid function normalizes result to lie between 0 and 1
        return 1 / (1 + np.exp(weight_sum * -1))
    def train(self, train_output, train_input, iterations):
        while(iterations > 0):
            iterations-=1
            #Calculate Guess
            output = self.calc_output(train_input)
            #Calculate Error in Guess
            error = train_output - output
            #Adjust Weights by Error Derivative Formula
            adjust = np.dot(train_input.T, error * output * (1-output))
            self.weight += adjust
        
        
        
        
        
        