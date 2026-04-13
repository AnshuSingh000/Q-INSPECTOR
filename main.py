from examples.sample_circuits import circuit_hh, circuit_xx, circuit_cxcx, circuit_mixed
from qinspector.validator import validate_circuit
from qinspector.optimizer import optimize_circuit
from qinspector.scorer import compute_score


def print_circuit(title, qc):
    print(f"\n=== {title} ===")

    print("\nOriginal circuit:")
    print(qc)
    original_gate_count = len(qc.data)
    print("Original gate count:", original_gate_count)

    findings = validate_circuit(qc)
    print("\nValidation findings:")
    if findings:
        for f in findings:
            print("-", f)
    else:
        print("- No issues found")

    optimized_qc, applied_rules = optimize_circuit(qc.copy())

    print("\nOptimized circuit:")
    print(optimized_qc)
    optimized_gate_count = len(optimized_qc.data)
    print("Optimized gate count:", optimized_gate_count)

    reduction = original_gate_count - optimized_gate_count
    percentage = (reduction / original_gate_count) * 100 if original_gate_count > 0 else 0

    print("\nOptimization metrics:")
    print("Gate reduction:", reduction)
    print(f"Reduction percentage: {percentage:.2f}%")

    original_score = compute_score(qc)
    optimized_score = compute_score(optimized_qc)

    print("\nCircuit scores:")
    print("Original score:", original_score)
    print("Optimized score:", optimized_score)

    if percentage > 50:
        print("⚡ Significant optimization achieved")

    print("\nApplied optimization rules:")
    if applied_rules:
        for rule in applied_rules:
            print("-", rule)
    else:
        print("- No optimization rules applied")


def main():
    print_circuit("HH Circuit", circuit_hh())
    print_circuit("XX Circuit", circuit_xx())
    print_circuit("CXCX Circuit", circuit_cxcx())
    print_circuit("Mixed Circuit", circuit_mixed())


if __name__ == "__main__":
    main()