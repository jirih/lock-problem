class SolutionWriter(object):
    def __init__(self):
        pass

    def write(self, solutions):
        print("Number of solutions found: %d" % len(solutions))
        for solution in solutions:
            print(solution)


