class LockSolver(object):
    def __init__(self, number_of_digits, rules):
        self.number_of_digits = number_of_digits
        self.rules = rules
        #print(self.number_of_digits)
        #for r in self.rules:
        #    print(r)

    def add_leading_zeros(self, n):
        return str(n).zfill(self.number_of_digits)

    def solve(self):
        all_combinations = [self.add_leading_zeros(n) for n in range(10**self.number_of_digits)]
        solutions = [c for c in all_combinations if self.all_rules_passed(c)]
        return solutions

    def all_rules_passed(self, c):
        for rule in self.rules:
            if not rule.is_passing(c):
                return False
        return True
