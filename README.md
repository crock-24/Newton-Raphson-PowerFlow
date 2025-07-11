# Fast Decoupled Newton-Raphson Power Flow Method

---

## Overview

This Python script implements the Fast Decoupled Newton-Raphson (FDNR) method for solving power flow problems in electrical power systems. It is designed to compute bus voltages and angles in a simplified 3-bus power network using iterative numerical techniques.

The FDNR method is a widely used technique in power systems for efficiently solving nonlinear load flow equations by decoupling real and reactive power calculations.

---

## Features

- Defines the admittance matrix (`Ybus`) for a 3-bus system with complex impedances.
- Converts admittance values into susceptance matrix (`Bmatrix`).
- Constructs Jacobian matrices necessary for the FDNR iterative solution.
- Iteratively solves for bus voltage angles (`delta`) and voltage magnitudes (`V`) based on scheduled real (`P`) and reactive (`Q`) power injections.
- Calculates the voltage and current phasors at each bus.
- Computes apparent power flows and line losses in the network.
- Checks power balance consistency in the system.

---
## Three Bus Impedance Network

<img width="763" height="461" alt="image" src="https://github.com/user-attachments/assets/168c182b-f9d4-4118-87f1-fd38d8cf1ffc" />

---

## Requirements

- Python 3.x
- Libraries:
  - `numpy`
  - `cmath`
  - `math`
