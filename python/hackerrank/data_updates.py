
#!/usr/bin/python
"""
A data analyst recently joined hackerRank as an intern.

As an initial task, data for n days is provided to the intern.
Then, k updates are perfomedon the data, where each update is of the form[i, r].
This indicates that the subarray of data starting at index i and ending at index r is negated.

For example if data = [1, 2, 3, 4] and the updates are [2, 4], then the data becomes
data = [1, -2, -3, -4]

Given the initial data and k updates, find the final data after all updates.
NOTE 1-based indexing is used.

Example
n = 4
data = [1, -4, -5, 2]
k = 2
updates = [[2,4], [1,2]]

1. After update one: data = [1, 4, 5,-2]
2. After update two: data = [-1, -4, 5, -2]

The final data is [-1, -4, 5, -2]
"""
"""

The problem, we need to do k updates to given data,
in each update, we're negating the elements in the update indexes given(1-based)
Steps:
    1. Create a function that does an individual update in the list of updates given:
    store the updated data in the same index in the new array.
    2. Loop through the data and updates performing each individual update and return the final result
    3. Ensure the data does not go out of range

TODO Rethink this process and redo the task.
"""
def ind_updates(data, update):
    # performs individual updates
    new_data = data
    
    for val in update:
        for d in data:
            index = data.index(d)
            if index == val:
                d = d * -1
            new_data[index] = d

    return new_data

def getFinalData(data, updates):
    # Write your code here
    update = []
    
    for k in updates:
        new_data = ind_updates(data, k)
        update.append(new_data)

    length = len(update)
    return new_data