from examples.sample_circuits import circuit_hh, circuit_xx, circuit_cxcx, circuit_mixed
from qinspector.validator import validate_circuit
from qinspector.optimizer import optimize_circuit


def print_circuit(title, qc):
    print(f"\n=== {title} ===")

    print("\nOriginal circuit:")
    print(qc)
    print("Original gate count:", len(qc.data))

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
    print("Optimized gate count:", len(optimized_qc.data))

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