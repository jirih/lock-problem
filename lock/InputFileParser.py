import os
import re

from LockException import LockException
from RuleAllWrong import RuleAllWrong
from RuleCorrect import RuleCorrect
from RuleWrongPlace import RuleWrongPlace
from XRuleCorrect import XRuleCorrect
from XRuleWrongPlace import XRuleWrongPlace
from ZRuleCorrect import ZRuleCorrect
from ZRuleWrongPlace import ZRuleWrongPlace


class InputFileParser(object):
    def __init__(self, file):
        self.number_of_digits = 0
        self.rules = []

        if os.path.exists(file):
            with open(file, 'rb') as f:
                try:
                    for line in f.readlines():
                        self._parse_line(line)
                except OSError as e:
                    raise LockException("Error when reading %s." % file)

        else:
            raise LockException("File %s does not exist." % file)

    def _parse_line(self, line):
        line = line.decode("utf-8").strip()
        #print(line)
        tokens = re.split('\s+', line)
        #print(tokens)
        if tokens[0] == "digits":
            self.number_of_digits = int(tokens[1])
            return
        if tokens[0] == "correct":
            self.rules.append(RuleCorrect(int(tokens[1]), tokens[2]))
            return
        if tokens[0] == "wrongplace":
            self.rules.append(RuleWrongPlace(int(tokens[1]), tokens[2]))
            return
        if tokens[0] == "allwrong":
            self.rules.append(RuleAllWrong(tokens[1]))
            return
        if tokens[0] == "xcorrect":
            self.rules.append(XRuleCorrect(int(tokens[1]), tokens[2]))
            return
        if tokens[0] == "xwrongplace":
            self.rules.append(XRuleWrongPlace(int(tokens[1]), tokens[2]))
            return
        if tokens[0] == "zcorrect":
            self.rules.append(ZRuleCorrect(int(tokens[1]), tokens[2]))
            return
        if tokens[0] == "zwrongplace":
            self.rules.append(ZRuleWrongPlace(int(tokens[1]), tokens[2]))
            return

        raise LockException("Line not understood: %s" % line)

    def get_rules(self):
        return self.rules

    def get_number_of_digits(self):
        return self.number_of_digits
