# inp = open('input2_1.text', 'r')
# out = open('output2_1.text', 'w')

inp = open('input2_2.text', 'r')
out = open('output2_2.text', 'w')

# inp = open('input2_3.text', 'r')
# out = open('output2_3.text', 'w')

# inp = open('input2_4.text', 'r')
# out = open('output2_4.text', 'w')


###############################################
# The main idea is to sort the activities by their start time
# and then to check if the end time of the previous activity is
# less than the start time of the next activity
# if it is, then we add the activity to the result array,
# and then we sort the activities by their end time
# and do the same thing
# then we compare the length of the result arrays and print the
# bigger one
###############################################


first_line = inp.readline().split()

activities_num = int(first_line[0])
people_num = int(first_line[1])

people = {}
activities = [[] for i in range(activities_num)]

for i in range(people_num):
    people[i] = []

for i in range(activities_num):
    activities[i] = []

for i in range(activities_num):
    line = inp.readline().split()
    activities[i].append(int(line[0]))
    activities[i].append(int(line[1]))

for i in range(1, people_num):
    people[i] = []

activities.sort(key=lambda x: x[0])

people[0].append(activities[0])

for i in range(1, activities_num):
    node = False
    for value in people.values():
        if activities[i] in value:
            continue
        else:
            if len(value) != 0:
                if value[-1][1] <= activities[i][0]:
                    value.append(activities[i])
                    break
                else:
                    continue
            else:
                value.append(activities[i])
                break


count = 0
for value in people.values():
    count += len(value)


###############################################

reverse_people = {}
for i in range(0, people_num):
    reverse_people[i] = []

activities.sort(key=lambda x: x[1])

reverse_people[0].append(activities[0])

for i in range(1, activities_num):
    node = False
    for value in reverse_people.values():
        if activities[i] in value:
            continue
        else:
            if len(value) != 0:
                if value[-1][1] <= activities[i][0]:
                    value.append(activities[i])
                    break
                else:
                    continue
            else:
                value.append(activities[i])
                break

rev_count = 0
for value in reverse_people.values():
    rev_count += len(value)


out.write(str(max(count, rev_count)))

