from Rule import Rule


class RuleWrongPlace(Rule):
    def __init__(self, m, digits):
        self.m = m
        self.digits = digits

    def is_passing(self, test_digits: str) -> bool:
        test_digits_length = self._get_length(test_digits)

        n = 0
        for i in range(test_digits_length):
            if self._is_at_wrong_place(test_digits[i], i):
                n += 1

        #print(self, test_digits, n, n == self.m)

        return n == self.m

    def __str__(self):
        return "RuleWrongPlace(%d, %s)" % (self.m, self.digits)
