
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

matplotlib.use("TkAgg")

def draw_gantt_chart(segments, parent_frame):
    if not segments:
        return

    unique_pids = sorted(set(s['pid'] for s in segments))
    colors = {}
    rng = random.Random(42)
    for pid in unique_pids:
        colors[pid] = '#9e9e9e' if pid == 'Idle' else (rng.random(), rng.random(), rng.random())

    fig, ax = plt.subplots(figsize=(9, 3))
    fig.patch.set_facecolor("#FFFFFF")
    ax.set_facecolor("#FAFAFA")
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color("#999999")

    for seg in segments:
        pid = seg['pid']
        start = seg['start']
        end = seg['end']
        width = end - start
        ax.barh(0, width, left=start, color=colors[pid], edgecolor='black', height=0.6)
        ax.text(start + width / 2, 0, pid, ha='center', va='center',
                color='white' if pid != 'Idle' else 'black', fontsize=9)

    ax.set_xlim(0, max(s['end'] for s in segments))
    ax.set_xlabel("Time", fontsize=10)
    ax.set_yticks([])
    ax.set_title("Gantt Chart (Preemptive SJF / SRTF)", fontsize=12, fontweight='bold', color="#333333")

    xticks = sorted(set([s['start'] for s in segments] + [s['end'] for s in segments]))
    ax.set_xticks(xticks)

    handles = [matplotlib.patches.Patch(color=colors[p], label=p) for p in unique_pids if p != 'Idle']
    if handles:
        ax.legend(handles=handles, loc='upper right', fontsize=8, title="Processes")

    canvas = FigureCanvasTkAgg(fig, master=parent_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)
