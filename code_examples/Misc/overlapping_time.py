def overlapping_time(start, end):
    overseer = {}
    firstMeeting = {}
    count = 0
    for each in start:  # O(n)
        count += 1
        if count == 1:
            firstMeeting[each] = end[0]
        overseer[each] = end[0]

    for each in overseer:
        for inner_each in firstMeeting:
            if firstMeeting[inner_each] >= each:
                print(each, firstMeeting[inner_each])  # O(n^2)

overlapping_time([1, 2, 3, 4], [2, 3, 5, 6])