# QInspector

Explainable pre-execution validation and optimization of quantum circuits.

QInspector is a lightweight prototype built using Python and Qiskit. It analyzes quantum circuits before execution, detects redundant gate patterns, and simplifies circuits using rule-based transformations.

## Why QInspector?
Quantum hardware is highly sensitive to noise, and unnecessary gates increase execution cost and error probability. QInspector helps reduce redundant operations before execution.

## Current Features
- Detects redundant consecutive gates
- Supports simplification of:
  - H-H
  - X-X
  - Z-Z
  - CX-CX
- Shows original vs optimized circuit
- Reports validation findings
- Explains applied optimization rules
- Displays gate count reduction

## Project Structure
- `examples/` — sample circuits for testing
- `qinspector/validator.py` — validation logic
- `qinspector/optimizer.py` — optimization logic
- `qinspector/utils.py` — helper functions
- `qinspector/rules.py` — supported cancellation rules
- `main.py` — full multi-circuit run
- `demo.py` — focused demo for presentation

## Installation
```bash
pip install -r requirements.txt