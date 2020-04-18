from Rule import Rule


class XRuleWrongPlace(Rule):
    def __init__(self, m, digits):
        self.m = m
        self.digits = digits

    def is_passing(self, test_digits: str) -> bool:
        test_digits_length = self._get_length(test_digits)

        n = 0
        for i in range(test_digits_length):
            if self._is_at_wrong_place(test_digits[i], i):
                n += 1

        k = 0
        for i in range(test_digits_length):
            if self._is_at_right_place(test_digits[i], i):
                k += 1

        #print(self, test_digits, n, n >= self.m, k == 0)

        return n >= self.m and k == 0

    def __str__(self):
        return "XRuleWrongPlace(%d, %s)" % (self.m, self.digits)
