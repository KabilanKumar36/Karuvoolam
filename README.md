# Karuvoolam (கருவூலம்) - CAE Data Exchange Toolkit

![Language](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python) ![Format](https://img.shields.io/badge/Formats-HDF5%20%7C%20PCH%20%7C%20JSON-orange) ![Domain](https://img.shields.io/badge/Domain-Data%20Engineering-green)

## 📁 Overview
**Karuvoolam** (Tamil for *Treasury* or *Archive*) is a suite of Python automation utilities designed to solve the **"Format Fragmentation"** problem in Computer-Aided Engineering (CAE).

It provides robust converters to bridge the gap between:
1.  **Legacy Simulation Outputs:** Nastran Punch files (`.pch`).
2.  **High-Performance Storage:** Hierarchical Data Format (`.h5` / HDF5).
3.  **Modern Analytics:** Data Science ready formats (`.csv`, `.json`).

## 🛠️ The Utility Belt

| Tool | Source Format | Target Format | Use Case |
| :--- | :--- | :--- | :--- |
| **PCH2CSV** | Nastran `.pch` | `.csv` | Converting legacy fixed-width simulation results into Pandas-readable tables. |
| **HDF2JSON** | HDF5 `.h5` | `.json` | Exposing binary simulation data to Web UIs or NoSQL databases. |
| **HDF2CSV** | HDF5 `.h5` | `.csv` | Flattening hierarchical data for Excel/Matlab analysis. |
| **FastReader** | `.csv` | Memory | Optimized large-file reader using chunking strategies. |

## 🔧 Technical Highlights
* **HDF5 Handling:** Uses `h5py` to recursively traverse groups and datasets, flattening nested structures into tabular formats.
* **Legacy Parsing:** Implements custom fixed-width parsing logic to handle the idiosyncratic formatting of Nastran Punch files (72-character limits, wrapped scientific notation).
* **Memory Efficiency:** Scripts are designed with generators to handle datasets larger than RAM.

## 📦 Dependencies
```txt
pandas>=1.3.0
h5py>=3.1.0
numpy>=1.21.0
