def compute_score(circuit):
    gate_count = len(circuit.data)

    # Simple scoring logic
    score = max(0, 100 - (gate_count * 10))

    return score