from examples.sample_circuits import circuit_mixed
from qinspector.validator import validate_circuit
from qinspector.optimizer import optimize_circuit


def demo():
    qc = circuit_mixed()

    print("\nQInspector Demo")
    print("=" * 50)

    print("\nOriginal circuit:")
    print(qc)
    print("Original gate count:", len(qc.data))

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
    print("Optimized gate count:", len(optimized_qc.data))

    reduction = len(qc.data) - len(optimized_qc.data)
    print(f"\nGate reduction: {reduction}")

    print("\nApplied optimization rules:")
    if applied_rules:
        for rule in applied_rules:
            print("-", rule)
    else:
        print("- No optimization rules applied")


if __name__ == "__main__":
    demo()