import os
import glob
from termcolor import colored
import unittest

def run_tests(root_path):
    # テストケースを自動的に取得
    test_files = glob.glob(os.path.join(root_path, "tests", "*.py"))

    if not test_files:
        print(colored("-"*50, 'red'))
        print(colored("No test cases found in the 'tests' folder.", 'red'))
        print(colored("-"*50, 'red'))
        return

    for test_file in test_files:
        print(colored(f"Running tests from: {test_file}", 'magenta'))
        test_suite = unittest.TestLoader().discover(os.path.dirname(test_file), os.path.basename(test_file))
        unittest.TextTestRunner(verbosity=2).run(test_suite)
        print()