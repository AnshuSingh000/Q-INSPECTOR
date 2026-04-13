from qiskit import QuantumCircuit


def circuit_hh():
    qc = QuantumCircuit(1)
    qc.h(0)
    qc.h(0)
    qc.x(0)
    return qc


def circuit_xx():
    qc = QuantumCircuit(1)
    qc.x(0)
    qc.x(0)
    qc.z(0)
    return qc


def circuit_cxcx():
    qc = QuantumCircuit(2)
    qc.cx(0, 1)
    qc.cx(0, 1)
    qc.h(1)
    return qc


def circuit_mixed():
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(0, 1)
    qc.x(1)
    qc.x(1)
    qc.z(0)
    return qc