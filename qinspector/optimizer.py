from qinspector.utils import same_gate_and_qubits


def optimize_circuit(circuit):
    new_data = []
    i = 0
    data = circuit.data

    while i < len(data):
        if i < len(data) - 1:
            inst1 = data[i]
            inst2 = data[i + 1]

            if same_gate_and_qubits(circuit, inst1, inst2):
                i += 2
                continue

        new_data.append(data[i])
        i += 1

    circuit.data = new_data
    return circuit