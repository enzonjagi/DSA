
#!/usr/bin/python
"""
The problem, we need to do k updates to given data,
in each update, we're negating the elements in the update indexes given(1-based)
Steps:
    1. Create a function that does an individual update in the list of updates given:
    store the updated data in the same index in the new array.
    2. Loop through the data and updates performing each individual update and return the final result
    3. Ensure the data does not go out of range
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