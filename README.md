
# Preemptive SJF (SRTF) Scheduling Simulator

## 📌 Overview
This project is a simulation of the **Preemptive Shortest Job First (SJF)** scheduling algorithm, also known as **Shortest Remaining Time First (SRTF)**. It is implemented in **Python** with a **Graphical User Interface (GUI)** using Tkinter and includes:

- User-defined number of processes
- Input fields for **Arrival Time (AT)** and **Burst Time (BT)**
- Validation for input data
- Calculation of:
  - Completion Time (CT)
  - Turnaround Time (TAT)
  - Waiting Time (WT)
  - Response Time (RT)
- Display of **average WT, TAT, RT**
- **Color-coded Gantt Chart** visualization

---

## ✅ Features
- **GUI-based input** for processes
- **Dynamic Gantt Chart** using Matplotlib
- **Modern styling** for better user experience

---

## 📂 Project Structure
sjf_project/
├── main.py        # GUI and integration
├── sjf.py         # Algorithm logic (Preemptive SJF)
├── chart.py       # Gantt chart drawing
├── style.py       # Styling and color palette
└── README.md      # Documentation
