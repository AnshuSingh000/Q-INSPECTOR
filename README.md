# QInspector

Explainable pre-execution validation and optimization of quantum circuits.

QInspector is a lightweight prototype built using Python and Qiskit. It analyzes quantum circuits before execution, detects redundant gate patterns, and simplifies circuits using rule-based transformations.

## Why QInspector?
Quantum hardware is highly sensitive to noise, and unnecessary gates increase execution cost and error probability. QInspector helps reduce redundant operations before execution while also explaining what was removed and why.

## Current Features
- Detects redundant consecutive gates
- Supports simplification of:
  - H-H
  - X-X
  - Y-Y
  - Z-Z
  - CX-CX
  - CZ-CZ
- Shows original vs optimized circuit
- Reports validation findings
- Explains applied optimization rules
- Displays gate count reduction
- Computes simple circuit quality scores
- Exports circuit diagrams as images

## Project Structure
- `examples/` — sample circuits for testing
- `qinspector/validator.py` — validation logic
- `qinspector/optimizer.py` — optimization logic
- `qinspector/utils.py` — helper functions
- `qinspector/rules.py` — supported cancellation rules
- `qinspector/scorer.py` — circuit scoring
- `qinspector/analyzer.py` — optimization verdicts
- `qinspector/visualizer.py` — image export
- `main.py` — full multi-circuit run
- `demo.py` — focused demo for presentation

## Installation
```bash
pip install -r requirements.txt