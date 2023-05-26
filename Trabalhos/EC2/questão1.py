'''

===========================================================================
Problem: Consider an exam with 'n' questions. Each question 'i' has a value
'vi' > 0 and demands 'mi' > 0 minutes to be solved. Calculate the minimum
of minutes needed to get at least 'P' points in the test.
===========================================================================

'''


def line():
    print('==' * 40)


def Header():
    print('\n')
    line()
    print(f'\n{"Author: Vítor Sallenave Sales Milome":^75}\n')
    line()
    print('\n')


def CreateMemory(p, value):
    return [[-1 for _ in range(p+1)] for _ in range(value)]


def PrintMemory(memo):
    li, co = len(memo), len(memo[0])

    line()
    print('\nMemory:\n')
    for i in range(li):
        l = list()
        for j in range(co):
            l.append(memo[i][j])
        print(f'\t{l}')
    print('\n')
    line()


def M(i, v):
    if v == 0:
        return 0
    elif v < 0:
        return float('inf')
    else:
        if memory[i][v] == -1:
            # There are two possibilities: do or not the question
            do_question = M(i-1, v - values[i]) + minutes[i]
            pass_question = M(i-1, v)
            memory[i][v] = min(do_question, pass_question)

        return memory[i][v]


Header()
# Questions values
values = [1, 2, 3, 4, 5]
n = len(values)
# Questions times (min)
minutes = [1, 3, 4, 6, 9]
# Minimum Points
P = int(input('How many points do you need to get approved? '))
# Creating a (P+1) X n matrix
memory = CreateMemory(P, n)
# Printing the answer and the memory view
answer = M(0, P)
PrintMemory(memory)
print(f'This {P} points can be achieved in {answer} minutes')