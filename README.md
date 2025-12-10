Name: Cole Tindall ctindal3

Module Info: || Module 14: Final Exam: Quantum Computation | 12/9/2025 11:59 PM

Approach: 

hadamard.py - 
This file defines the H gate child class of the SingleQubitOperator class from qoperators.py.
The constructor initializes the operator matrix by calling the parent class constructor, which stores the matrix internally.
This class then supplies the correct 2×2 H matrix and applies it to a qubit by multiplying the operator matrix with the qubit’s state vector.

paulix.py -

This file defines the X gate a child class of the SingleQubitOperator class.
It initializes the operator matrix using the parent constructor and stores the 2×2 matrix in the operator_matrix variable.
The class then uses the correct X matrix to operate on a qubit by multiplying the X gate matrix with the qubit’s current state.

qoperators.py -
This script contains the parent class SingleQubitOperator responsible for initializing and storing a 2×2 matrix.
It serves as the base class for both the Hadamard and X gates and enforces required methods through the abstract operate() method, as specified in the assignment reqs.

qubit.py -
This script creates the Qubit class. The constructor initializes the qubit’s state as a 2×1 column vector using the provided alpha and beta values from qubits.txt.
The validate_amplitudes method checks that the sum of the squares of alpha and beta equals 1. If this condition is not met, the method prints "Invalid probability amplitude(s)".
The experiment method simulates repeated measurements using a weighted random process based on the probability amplitudes. This demonstrates the likelihood of the qubit to be at a 0 or 1 state.
Then the __str__ method formats the qubit state for output.

main.py -
This script controls the overall flow. It begins by defining a helper function that maps each operator character in the input file to either a Hadamard or X gate.
The main() function reads the qubits.txt file line by line, separates each line into alpha, beta, and the correct sequence of operators, and initializes a Qubit object using the provided values.
The program then calls validate_amplitudes to ensure state/probability is valid. If the amplitudes are not valid, the invalid message is printed and the program moves on to the next line.
If the amplitudes are valid, the program applies the specified operators in order and then runs the experiment to display the measurement results, followed by printing the final state of the qubit.

Known Bugs: 
qubit.py lines 19-->23 
    I could not figure out how to not have the output of the scripts have "Invalid probability amplitude(s)." twice so 
    I had to do do some googling and it said to set a tolerance value to compare due to how small the difference could be? 
    Would love to know why this is a thing, do not quite understand it... 

Citations: 



# Submitted files
ctindal3_mod14.docx
main.py
hadamard.py
paulix.py
qoperators.py
qubit.py
readme.txt

# Github Link :

