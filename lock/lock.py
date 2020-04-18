# -*- coding: utf-8 -*-
import argparse

from InputFileParser import InputFileParser
from LockSolver import LockSolver
from SolutionWriter import SolutionWriter


def create_parser():
    parser = argparse.ArgumentParser(description='Solve a lock problem')
    parser.add_argument('-f', '--file', dest='file', help='<Required> file', action='store')
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    file = args.file
    if file is not None:
        input_file_parser = InputFileParser(file)

        number_of_digits = input_file_parser.get_number_of_digits()
        rules = input_file_parser.get_rules()

        lock_solver = LockSolver(number_of_digits, rules)
        solutions = lock_solver.solve()

        solution_writer = SolutionWriter()
        solution_writer.write(solutions)
    else:
        print("Missing file argument.")


if __name__ == "__main__":
    main()
