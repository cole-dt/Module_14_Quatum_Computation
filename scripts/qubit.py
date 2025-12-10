import numpy as np
import random
from computingbit import ComputingBit

class Qubit(ComputingBit):
    def __init__(self, alpha, beta):
        # State uses a 2x1 NumPy column vector that is initialized here
        self.state = np.array([[alpha], [beta]])


    def validate_amplitudes(self):
        # Extract alpha and beta 
        alpha = self.state[0, 0]
        beta = self.state[1, 0]

        # Calculate the sum of squares using NP 
        sum_sq = np.sum(np.square(self.state))

        # Compare with a tolerance because if I do not it will output the Invalid probability amplitude(s) message twice?? Would love to know why??
        if np.abs(sum_sq - 1.0) > 1e-6:
            print("\nInvalid probability amplitude(s).")
            return False
        return True

    #  Method named probability_amplitudes that returns the probabilities of 0 vs 1
    def probability_amplitudes(self):
        prob_0 = self.state[0][0] * self.state[0][0]
        prob_1 = self.state[1][0] * self.state[1][0]
        return prob_0, prob_1

    def experiment(self):
        probabilities = self.probability_amplitudes()
        prob_0 = probabilities[0]
        prob_1 = probabilities[1]
        zeros_count = 0
        ones_count = 0
        
        for x in range(100):
            if random.random() < prob_0:
                zeros_count += 1
            else:
                ones_count += 1
        
        print("Percentage of 0's measured: ", zeros_count/100 )
        print("Percentage of 1's measured: ", ones_count/100 )


    # Provides a string representation for intial state as 'X|0> + Y|1>'.
    def __str__(self):
        alpha = self.state[0][0]
        beta = self.state[1][0]

        return str(alpha) + "|0> + " + str(beta) + "|1>"