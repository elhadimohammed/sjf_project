
import heapq

def sjf_preemptive(processes):
    processes.sort(key=lambda x: x['arrival'])
    n = len(processes)
    time = 0
    completed = 0
    i = 0
    ready = []
    remaining = {p['pid']: p['burst'] for p in processes}
    first_start = {p['pid']: None for p in processes}
    completion = {p['pid']: None for p in processes}
    timeline = []

    while completed < n:
        while i < n and processes[i]['arrival'] <= time:
            pid_i = processes[i]['pid']
            heapq.heappush(ready, (remaining[pid_i], pid_i))
            i += 1

        if ready:
            rt, pid = heapq.heappop(ready)
            if first_start[pid] is None:
                first_start[pid] = time
            timeline.append((time, pid))
            remaining[pid] -= 1
            time += 1
            if remaining[pid] > 0:
                heapq.heappush(ready, (remaining[pid], pid))
            else:
                completion[pid] = time
                completed += 1
        else:
            timeline.append((time, 'Idle'))
            time += 1

    # Compress timeline
    segments = []
    if timeline:
        seg_pid = timeline[0][1]
        seg_start = timeline[0][0]
        prev_time = seg_start
        for t, pid in timeline[1:]:
            if pid == seg_pid and t == prev_time + 1:
                prev_time = t
            else:
                segments.append({'pid': seg_pid, 'start': seg_start, 'end': prev_time + 1})
                seg_pid = pid
                seg_start = t
                prev_time = t
        segments.append({'pid': seg_pid, 'start': seg_start, 'end': prev_time + 1})

    results = []
    for p in processes:
        pid = p['pid']
        AT = p['arrival']
        BT = p['burst']
        CT = completion[pid]
        TAT = CT - AT
        WT = TAT - BT
        RT = first_start[pid] - AT
        results.append({'pid': pid, 'AT': AT, 'BT': BT, 'CT': CT, 'TAT': TAT, 'WT': WT, 'RT': RT})

    return segments, results
