from qubit import Qubit
from hadamard import Hadamard
from paulix import PauliX

def create_operator_instance(op_char):
    if op_char == "H":
        return Hadamard()
    elif op_char == "X":
        return PauliX()
    else:
        return None

def main():
    with open("qubits.txt", "r") as f:
        for line in f:
            lines = line.strip().split()

            #  Floating points for alphas and beta
            alpha = float(lines[0])
            beta = float(lines[1])
            # Operators that follow after pulled from list
            operators = lines[2:]

            # Create qubit object from alpha,beta 
            current_qubit = Qubit(alpha, beta)

            # use validate_amplitudes if amplitudes are invalid
            if not current_qubit.validate_amplitudes():
                continue
            # Valid amplitudes so proceed
            print()
            print("Initial state:", current_qubit)

            # Validate operators are X,H if not stop and print Invalid Operators
            valid_ops = True
            for op_char in operators:
                if create_operator_instance(op_char) is None:
                    print("Invalid Operator.")
                    valid_ops = False
                    break

            if not valid_ops:
                continue

            # Apply operators
            for op_char in operators:
                operator = create_operator_instance(op_char)
                current_qubit = operator.operate(current_qubit)

            current_qubit.experiment()
            print("Final state: ", current_qubit)

if __name__ == "__main__":
    main()
