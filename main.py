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



# use all functions
def main():
    num_of_workers = int(input('How many are present tonight? '))
    present_workers = get_workers(num_of_workers)
    # print('DEBUG', present_workers)
    last_assignments = get_last_assignments(present_workers)
    # print('DEBUG', last assignments)
    if num_of_workers == 3:
        assignments = THREE
        unit_one = assignments[random.randint(0,2)]
        unit_two = assignments[random.randint(0,2)]
        unit_three = assignments[random.randint(0,2)]
        while unit_two == unit_one or unit_two == unit_three:
            unit_two = assignments[random.randint(0,2)]
        while unit_three == unit_one or unit_three == unit_two:
            unit_three = assignments[random.randint(0,2)]
        print({
            present_workers[0]: unit_one,
            present_workers[1]: unit_two,
            present_workers[2]: unit_three
        })
    elif num_of_workers == 2:
        assignments = TWO
        unit_one = assignments[random.randint(0,1)]
        unit_two = assignments[random.randint(0,1)]
        while unit_two == unit_one:
            unit_two = assignments[random.randint(0,1)]
        print({
            present_workers[0]: unit_one,
            present_workers[1]: unit_two
        })
    else:
        print({present_workers[0]: ['AC']})


if __name__ == '__main__':
    main()
