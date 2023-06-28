"""

===========================================================================
Problem: Given n tasks with a specific time to start and finish, determine
the maximum tasks that a processor can execute.
===========================================================================

"""


def line():
    print('==' * 40)


def Header():
    print('\n')
    line()
    print(f'\n{"Author: Vítor Sallenave Sales Milome ©":^75}\n')
    line()
    print('\b')


def ReadTasks():
    # Functions to return a sorting criteria
    def SortingCriteria(array):
        return array[1]

    # Reading the initial parameters
    t = int(input('\bEnter a value for the number of tasks: '))

    # Reading the information about the tasks
    entry = list()
    for i in range(t):
        info = input(f'\nType the start and the end of the task [{i + 1}]: ').split()
        s, e = int(info[0]), int(info[1])
        entry.append([s, e])
    print('\b')
    line()
    print('\b')

    # Sorting the entry by the end
    sorted_entry = sorted(entry, key=SortingCriteria)

    return sorted_entry


def SelectionTasks(entry):
    # Initial values
    tasks, k = 1, 0

    for i in range(1, len(entry)):
        # In this case, we can go ahead in order to reach the final
        if entry[i][0] >= entry[k][1]:
            k = i
            tasks += 1

    return tasks


def main():
    Header()
    entry = ReadTasks()
    print(f'\bYour entry is: {entry}\n')
    line()
    print(f'\nThe quantity of tasks executed by the processor was: {SelectionTasks(entry)}')


main()