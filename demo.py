from examples.sample_circuits import circuit_mixed
from qinspector.validator import validate_circuit
from qinspector.optimizer import optimize_circuit
from qinspector.scorer import compute_score
from qinspector.utils import gate_histogram
from qinspector.analyzer import optimization_verdict
from qinspector.visualizer import save_circuit_diagram


def demo():
    qc = circuit_mixed()

    print("\nQInspector Demo")
    print("=" * 50)

    print("\nOriginal circuit:")
    print(qc)
    original_gate_count = len(qc.data)
    print("Original gate count:", original_gate_count)
    print("Original gate distribution:", gate_histogram(qc))

    findings = validate_circuit(qc)
    print("\nValidation findings:")
    if findings:
        for finding in findings:
            print("-", finding)
    else:
        print("- No issues found")

    optimized_qc, applied_rules = optimize_circuit(qc.copy())

    print("\nOptimized circuit:")
    print(optimized_qc)
    optimized_gate_count = len(optimized_qc.data)
    print("Optimized gate count:", optimized_gate_count)
    print("Optimized gate distribution:", gate_histogram(optimized_qc))

    reduction = original_gate_count - optimized_gate_count
    percentage = (reduction / original_gate_count) * 100 if original_gate_count > 0 else 0

    print("\nOptimization metrics:")
    print("Gate reduction:", reduction)
    print(f"Reduction percentage: {percentage:.2f}%")
    print("Analysis verdict:", optimization_verdict(percentage))

    original_score = compute_score(qc)
    optimized_score = compute_score(optimized_qc)

    print("\nCircuit scores:")
    print("Original score:", original_score)
    print("Optimized score:", optimized_score)

    print("\nApplied optimization rules:")
    if applied_rules:
        for rule in applied_rules:
            print("-", rule)
    else:
        print("- No optimization rules applied")

    save_circuit_diagram(qc, "outputs/mixed_original.png")
    save_circuit_diagram(optimized_qc, "outputs/mixed_optimized.png")

    print("\nSaved circuit images:")
    print("- outputs/mixed_original.png")
    print("- outputs/mixed_optimized.png")


if __name__ == "__main__":
    demo()