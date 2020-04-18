from LockException import LockException


class Rule(object):
    def is_passing(self, test_digits: str) -> bool:
        raise NotImplementedError("Must be overridden.")

    def _get_length(self, test_digits):
        if len(test_digits) != len(self.digits):
            raise LockException("Length mismatch: %s %s" % (self.digits, test_digits))
        return len(test_digits)

    def _is_at_right_place(self, test_digit, place):
        return test_digit == self.digits[place]

    def _is_at_wrong_place(self, test_digit, place):
        return test_digit != self.digits[place] and test_digit in self.digits
