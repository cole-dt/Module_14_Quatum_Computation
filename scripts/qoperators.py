from abc import ABC, abstractmethod

class SingleQubitOperator(ABC):
    # Constructor to initialize instance variable matrix
    def __init__(self, operator_matrix):
        self.operator_matrix = operator_matrix

    # Abstract method called operate  as required 
    @abstractmethod
    def operate(self, qubit):
        pass
