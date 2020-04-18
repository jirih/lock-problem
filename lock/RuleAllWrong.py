from Rule import Rule


class RuleAllWrong(Rule):
    def __init__(self, digits):
        self.digits = digits

    def is_passing(self, test_digits: str) -> bool:
        test_digits_length = self._get_length(test_digits)

        n = 0
        for i in range(test_digits_length):
            if test_digits[i] not in self.digits:
                n += 1

        #print(self, test_digits, n, n == len(self.digits))

        return n == len(self.digits)

    def __str__(self):
        return "RuleAllWrong(%s)" % self.digits
