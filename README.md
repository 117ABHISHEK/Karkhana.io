# Möbius Strip 3D Model

This Python script models a **Möbius strip** using parametric equations and computes two important geometric properties:

- **Surface Area**
- **Edge Length**

It also visualizes the 3D strip using `matplotlib`.

---

## 📌 Features

- Parametric modeling of a Möbius strip
- Numerical computation of:
  - Surface area using cross product of partial derivatives
  - Edge length approximation along the boundaries
- Interactive 3D visualization

---

## 🧮 Parametric Equations Used

The Möbius strip is modeled using the following equations:

x(u,v) = (R + v * cos(u/2)) * cos(u)
y(u,v) = (R + v * cos(u/2)) * sin(u)
z(u,v) = v * sin(u/2)

Where:

- `u ∈ [0, 2π]` — angular parameter
- `v ∈ [-w/2, w/2]` — width-wise offset
- `R` — radius from the center to the strip
- `w` — width of the strip

---

## 🚀 Usage

### 🖥️ Run the Script

python mobius_strip.py

📥 Input Parameters
The script will prompt you for:

R: Radius (e.g., 1.0)

w: Width of the strip (e.g., 1.0)

n: Resolution (number of points, e.g., 100)

Example:

1.0
1.0
100

📤 Output
Printed surface area and edge length

A 3D plot of the Möbius strip

📦 Requirements
Install dependencies using:


pip install numpy matplotlib
📂 Project Structure

mobius_strip.py   # Main script with MobiusStrip class
README.md         # Project documentation

📸 Visualization
The script uses matplotlib to generate a 3D surface plot:


📘 How It Works
Mesh Grid: Uses np.meshgrid to generate a grid over (u, v).

Surface Area: Computed using the magnitude of the cross product of partial derivatives ru × rv.

Edge Length: Summed length along both boundaries v = ±w/2 using Euclidean distance.

Plotting: Uses plot_surface from mpl_toolkits.mplot3d.

🧠 Educational Value
This project demonstrates:

Parametric 3D geometry

Numerical integration (approximating surface area)

Vector calculus (cross product of partial derivatives)

Python object-oriented design

3D visualization using matplotlib


