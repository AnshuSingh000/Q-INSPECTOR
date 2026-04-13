from pathlib import Path
import matplotlib.pyplot as plt


def save_circuit_diagram(circuit, filepath):
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)

    figure = circuit.draw(output="mpl")
    figure.savefig(filepath, bbox_inches="tight")
    plt.close(figure)