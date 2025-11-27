# Rewrites the test files.
#
# Use this if the textconv scripts have been updated and
# the new output needs to be reflected in the baselines.
#
# Before committing the new baselines, make sure the difference
# with the previous version is as expected.

import os.path
from test_parse import parse


def run():
    rewrite_file("Test.amxd")
    rewrite_file("EncryptedTest.amxd")
    rewrite_file("FrozenTest.amxd")
    rewrite_file("WithGarbage.amxd")
    rewrite_file("Test.maxpat")
    rewrite_file("Test Project/Zipped.als")
    rewrite_file("Test Project/Test.als")
    rewrite_file("MalFormedJsonTest.maxpat")
    rewrite_file("ConflictMarkerTest.maxpat")


def rewrite_file(name: str):
    test_file_path = get_test_path_file("test_files/" + name)
    baseline_file_path = get_test_path_file("test_baselines/" + name + ".txt")

    with open(test_file_path, mode="r") as test_file:
        parsed = parse(test_file_path)

        with open(baseline_file_path, mode="w") as baseline_file:
            baseline_file.write(parsed)


def get_test_path_file(file_name):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), file_name))


if __name__ == "__main__":
    run()
