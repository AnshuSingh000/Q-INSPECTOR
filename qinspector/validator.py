from qinspector.rules import CANCELLING_SINGLE_QUBIT_GATES, CANCELLING_TWO_QUBIT_GATES
from qinspector.utils import get_gate_name, get_qubit_indices, same_gate_and_qubits


def validate_circuit(circuit):
    findings = []
    data = circuit.data

    for i in range(len(data) - 1):
        inst1 = data[i]
        inst2 = data[i + 1]

        if same_gate_and_qubits(circuit, inst1, inst2):
            gate_name = get_gate_name(inst1)
            qubits = get_qubit_indices(circuit, inst1)

            if gate_name in CANCELLING_SINGLE_QUBIT_GATES:
                findings.append(
                    f"Redundant '{gate_name}' gates on qubit(s) {qubits}"
                )

            elif gate_name in CANCELLING_TWO_QUBIT_GATES:
                findings.append(
                    f"Redundant '{gate_name}' gates on qubit(s) {qubits}"
                )

    return findings