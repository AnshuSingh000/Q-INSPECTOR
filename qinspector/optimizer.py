from qinspector.utils import get_gate_name, get_qubit_indices, same_gate_and_qubits


def optimize_circuit(circuit):
    new_data = []
    applied_rules = []
    i = 0
    data = circuit.data

    while i < len(data):
        if i < len(data) - 1:
            inst1 = data[i]
            inst2 = data[i + 1]

            if same_gate_and_qubits(circuit, inst1, inst2):
                gate_name = get_gate_name(inst1)
                qubits = get_qubit_indices(circuit, inst1)

                applied_rules.append(
                    f"Removed redundant '{gate_name}' gates on qubit(s) {qubits} because applying the same gate twice cancels its effect"
                )

                i += 2
                continue

        new_data.append(data[i])
        i += 1

    circuit.data = new_data
    return circuit, applied_rules