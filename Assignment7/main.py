inp = open("input2_4.text", "r")
out = open("output2_4.text", "w")

n, m = map(int, inp.readline().split())
activities = []
for _ in range(n):
    activities.append(list(map(int, inp.readline().split())))
activities.sort(key=lambda x: x[1])

completed_count = 0
assigned_end_times = [0] * m

for i in range(n):
    for j in range(m):
        if activities[i][0] >= assigned_end_times[j]:
            completed_count += 1
            assigned_end_times[j] = activities[i][1]
            break


print(completed_count)
out.write(str(completed_count))
out.close()