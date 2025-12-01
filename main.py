
import tkinter as tk
from tkinter import ttk, messagebox
from sjf import sjf_preemptive
from chart import draw_gantt_chart
from style import apply_style

def run_simulation():
    for widget in frame_chart.winfo_children():
        widget.destroy()
    try:
        n = int(entry_num.get().strip())
        if n <= 0 or n > 50:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number of processes (1–50).")
        return

    processes = []
    for i in range(n):
        try:
            at = int(arrival_entries[i].get())
            bt = int(burst_entries[i].get())
            if at < 0 or bt <= 0:
                raise ValueError
            processes.append({'pid': f'P{i+1}', 'arrival': at, 'burst': bt})
        except ValueError:
            messagebox.showerror("Error", f"Invalid input for process P{i+1}.")
            return

    segments, results = sjf_preemptive(processes)

    for row in tree.get_children():
        tree.delete(row)

    total_wt = total_tat = total_rt = 0
    for r in results:
        tree.insert("", "end", values=(r['pid'], r['AT'], r['BT'], r['CT'], r['TAT'], r['WT'], r['RT']))
        total_wt += r['WT']
        total_tat += r['TAT']
        total_rt += r['RT']

    avg_wt = total_wt / len(results)
    avg_tat = total_tat / len(results)
    avg_rt = total_rt / len(results)
    label_avg.config(text=f"Avg WT: {avg_wt:.2f} | Avg TAT: {avg_tat:.2f} | Avg RT: {avg_rt:.2f}")

    draw_gantt_chart(segments, frame_chart)

def create_input_fields():
    for widget in frame_inputs.winfo_children():
        widget.destroy()
    arrival_entries.clear()
    burst_entries.clear()
    try:
        n = int(entry_num.get().strip())
        if n <= 0 or n > 50:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number of processes first.")
        return

    tk.Label(frame_inputs, text="PID", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=6, pady=6)
    tk.Label(frame_inputs, text="Arrival Time (AT)", font=("Arial", 10, "bold")).grid(row=0, column=1, padx=6, pady=6)
    tk.Label(frame_inputs, text="Burst Time (BT)", font=("Arial", 10, "bold")).grid(row=0, column=2, padx=6, pady=6)

    for i in range(n):
        tk.Label(frame_inputs, text=f"P{i+1}", font=("Arial", 9)).grid(row=i+1, column=0, padx=6, pady=6)
        at_entry = tk.Entry(frame_inputs, width=10)
        bt_entry = tk.Entry(frame_inputs, width=10)
        at_entry.grid(row=i+1, column=1, padx=6, pady=6)
        bt_entry.grid(row=i+1, column=2, padx=6, pady=6)
        arrival_entries.append(at_entry)
        burst_entries.append(bt_entry)

root = tk.Tk()
root.title("Preemptive SJF Scheduling (Modular)")

top_frame = tk.Frame(root)
top_frame.pack(padx=10, pady=10, fill='x')

tk.Label(top_frame, text="Number of Processes:", font=("Arial", 10, "bold")).pack(side='left')
entry_num = tk.Entry(top_frame, width=8)
entry_num.pack(side='left', padx=6)

btn_create = tk.Button(top_frame, text="Create Fields", command=create_input_fields)
btn_create.pack(side='left', padx=6)

btn_run = tk.Button(top_frame, text="Run Simulation", command=run_simulation)
btn_run.pack(side='left', padx=6)

frame_inputs = tk.Frame(root, bd=2, relief='groove')
frame_inputs.pack(padx=10, pady=6, fill='x')

arrival_entries = []
burst_entries = []

columns = ("PID", "AT", "BT", "CT", "TAT", "WT", "RT")
tree = ttk.Treeview(root, columns=columns, show="headings", height=8)
for col in columns:
    tree.heading(col, text=col)
tree.pack(padx=10, pady=8, fill='x')

label_avg = tk.Label(root, text="", font=("Arial", 10, "bold"))
label_avg.pack(padx=10, pady=4)

frame_chart = tk.Frame(root)
frame_chart.pack(padx=10, pady=10, fill='both', expand=True)

entry_num.insert(0, "4")

apply_style(btn_create, btn_run)

root.mainloop()
