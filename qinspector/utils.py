def get_gate_name(instruction):
    return instruction.operation.name


def get_qubit_indices(circuit, instruction):
    return tuple(circuit.find_bit(qubit).index for qubit in instruction.qubits)


def same_gate_and_qubits(circuit, inst1, inst2):
    gate1 = get_gate_name(inst1)
    gate2 = get_gate_name(inst2)

    qubits1 = get_qubit_indices(circuit, inst1)
    qubits2 = get_qubit_indices(circuit, inst2)

    return gate1 == gate2 and qubits1 == qubits2