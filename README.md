# Geometric Modeling - Interpolating Triangular Patch Surfaces

This project implements a geometric modeling technique using **interpolating triangular patch surfaces**, based on the **Butterfly subdivision scheme**. The aim is to model and visualize smooth surfaces by iteratively refining a triangular mesh.

---

## 📌 Project Overview

We focus on implementing a mesh refinement algorithm for triangular surfaces using the Butterfly scheme. The implementation supports various 3D shapes (e.g., diamond, cube, tetrahedron) and allows for multiple levels of subdivision.

---

## 🧠 Method Principle

The **Butterfly subdivision scheme** is an interpolating method that constructs new points based on weighted averages of neighboring vertices, generating smoother surfaces while preserving initial vertex positions.

### Key Steps:
1. Each triangle is subdivided into 4 smaller triangles.
2. New vertices are computed using a linear combination of:
   - Midpoints of edges (1/2 weight),
   - Immediate neighbors (1/8 weight),
   - Distant neighbors (-1/16 weight).
3. This process is recursively applied for finer subdivisions.

---

## ✅ Advantages

- **Interpolating**: Original vertices are preserved.
- **Efficient**: Suitable for real-time and mesh refinement applications.
- **Flexible**: Works with any triangular mesh.

## ⚠️ Limitations

- Sensitive to irregular mesh topology.
- May produce artifacts near extraordinary vertices.
- Less suitable for very coarse initial meshes.

---

## 🧪 Testing Samples

Several 3D shapes were used to test and visualize the Butterfly subdivision:

| Shape        | File                                  | Description                        |
|--------------|---------------------------------------|------------------------------------|
| Diamond      | `losange3D.py` / `losange3D_subdivised.py` | Diamond-shaped mesh and its subdivision |
| Cube         | `cube3D.py` / `cube3D_subdivised.py`       | Basic cube model with refinement   |
| Tetrahedron  | `tetraedre3D.py` / `tetraedre3D_subdivised.py` | Regular tetrahedron subdivision    |

Each model is rendered using **matplotlib's 3D tools** and subdivided using the `butterfly_subdivision_loop` function.


---

## 🛠️ How to Run

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd geometric-modeling
   pip install matplotlib numpy
   python losange3D_subdivised.py
   ```

## 👩‍💻 Authors

- Kawtar Lyamoudi
- Bryan Chen

📜 License

This project is released under the MIT License.
