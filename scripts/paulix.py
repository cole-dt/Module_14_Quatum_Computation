import numpy as np
from qoperators import SingleQubitOperator

class PauliX(SingleQubitOperator):
    def __init__(self):
        operator_matrix = np.array([[0.0, 1.0],
                                    [1.0, 0.0]])
        SingleQubitOperator.__init__(self, operator_matrix)

    def operate(self, qubit):
        result_vector = np.dot(self.operator_matrix, qubit.state)
        qubit.state = result_vector
        return qubit
