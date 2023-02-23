"""Given an integer k represneting the number of people and a task array of size 2k having the duration of tasks.
Design a method which allocates a pair of tasks to each of them in a way that maximum time taken to complete them is the minimum.
"""
def taskAssignment(k, tasks):
    tasks_with_order = sorted([[tasks[i],i] for i in range(len(tasks))],key = lambda l:l[0])
    res = []
    while len(res) < k:
        res.append([tasks_with_order[len(res)][1],tasks_with_order[2*k - len(res) - 1][1]])
    return res