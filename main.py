import pandas as pd
import random

TWO = ['ZONE_1', 'ZONE_2']
THREE = ['ZONE_1', 'ZONE_2', 'AH']

# get names of all workers for the shift
def get_workers(num_workers):
    workers = []
    for i in range(num_workers):
        worker = input('Please name one worker: ')
        workers.append(worker)
    return workers



def get_last_assignments(workers):
    last_assignments = []
    for i in range(len(workers)):
        assignment = input(f'Please input last assignment for {workers[i]}: ')
        last_assignments.append(assignment)
    return last_assignments



def assign_zones(previous, zones):
    current = []
    for i in range(len(previous)):
        current.append('')
        current[i] = zones[random.randint(0,len(previous)-1)]
    while all(val == current[0] for val in current):
        current[random.randint(0,len(previous)-1)] = zones[random.randint(0,len(previous)-1)]
    return current

# use all functions
def main():
    num_of_workers = int(input('How many are present tonight? '))
    present_workers = get_workers(num_of_workers)
    # print('DEBUG', present_workers)
    last_assignments = get_last_assignments(present_workers)
    # print('DEBUG', last assignments)
    if num_of_workers == 3:
        assignments = THREE
        assigned_zones = assign_zones(last_assignments, assignments)
        for i in range(len(present_workers)):
            print(present_workers[i], assigned_zones[i])
    elif num_of_workers == 2:
        assignments = TWO
        assigned_zones = assign_zones(last_assignments, assignments)
        for i in range(len(present_workers)):
            print(present_workers[i], assigned_zones[i])
    else:
        print({present_workers[0]: ['AC']})


if __name__ == '__main__':
    main()
