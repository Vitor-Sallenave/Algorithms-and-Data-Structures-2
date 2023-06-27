"""

===========================================================================
Problem: Calculate the maximum profit you can generate by solving tasks in
basis in the workload of your company.
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


def Reference():
    print('\b')
    line()
    print('\n◼ Reference - https://youtu.be/zPtI8q9gvX8\n')


def ReadTasks():
    # Functions to return a sorting criteria
    def SortingCriteria1(array):
        return array[1]

    # Reading the initial parameters
    info = input('\bEnter a value for the workload and the number of tasks: ').split()
    w, t = int(info[0]), int(info[1])

    # Creating a tasks table to manage the workload
    tasks_table = [0] * w

    # Reading the information about the tasks
    entry = list()
    for i in range(t):
        info = input(f'\nType the deadline and the profit of the task [{i + 1}]: ').split()
        d, p = int(info[0]), int(info[1])
        entry.append([d, p])
    print('\b')
    line()
    print('\b')

    # Sorting the entry by the profit
    sorted_entry = sorted(entry, key=SortingCriteria1)

    return t, sorted_entry, tasks_table


def MaxProfit(t, entry, tasks_table):
    max_profit = 0

    for i in range(t - 1, -1, -1):
        # Task information
        interval = entry[i][0] - 1
        profit = entry[i][1]

        # Verifying if any tasks is being done in the time interval
        if tasks_table[interval] == 0:
            # Filling the time interval
            tasks_table[interval] = 1
            max_profit += profit
        else:
            # Verifying if there are previously available intervals
            for k in range(interval):
                if tasks_table[k] == 0:
                    # Filling the time interval
                    tasks_table[k] = 1
                    max_profit += profit
                    break

    return max_profit


def main():
    Header()
    t, entry, tasks_table = ReadTasks()
    print(f'\bYour entry is: {entry}\n')
    line()
    print(f'\nThe maximum profit that you can earn your job is {MaxProfit(t, entry, tasks_table)}')


main()