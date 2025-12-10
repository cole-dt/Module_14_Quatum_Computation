import numpy as np
from qoperators import SingleQubitOperator

class Hadamard(SingleQubitOperator):
    def __init__(self):
        sqrt2_inv = 1.0 / np.sqrt(2.0)

        operator_matrix = np.array([
            [sqrt2_inv,  sqrt2_inv],
            [sqrt2_inv, -sqrt2_inv]
        ])
        
        SingleQubitOperator.__init__(self, operator_matrix)

    def operate(self, qubit):
        result_vector = np.dot(self.operator_matrix, qubit.state)

        qubit.state = result_vector
        return qubit
