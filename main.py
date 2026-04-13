from examples.sample_circuits import circuit_hh, circuit_xx, circuit_cxcx, circuit_mixed
from qinspector.validator import validate_circuit


def print_circuit(title, qc):
    print(f"\n=== {title} ===")
    print(qc)
    print("Gate count:", len(qc.data))

    findings = validate_circuit(qc)

    print("Validation findings:")
    if findings:
        for f in findings:
            print("-", f)
    else:
        print("- No issues found")


def main():
    print_circuit("HH Circuit", circuit_hh())
    print_circuit("XX Circuit", circuit_xx())
    print_circuit("CXCX Circuit", circuit_cxcx())
    print_circuit("Mixed Circuit", circuit_mixed())


if __name__ == "__main__":
    main()