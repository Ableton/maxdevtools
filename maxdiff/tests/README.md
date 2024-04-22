# Testing

The tests allow us to make sure we didn't accidentally change something to the patch printing script that changes its output in an unintended way.

## Running the tests

From the `maxdiff` folder, run `python3 tests/test.py`

## Changing the script

Whenever adding something to the patch printer script, ideally this change is covered by the test files, such as `test_files/Test.amxd`. After checking that the resulting patch summary differs only in the expected way, the new result from the script should then be saved in their baselines in `test_baselines/`. 

To rewrite all test baselines automatically, you can run `python3 ./maxdiff/tests/test_rewrite_baselines.py` from the repo root.

Every commit to this repository that changes the output of the scripts should be accompanied by a change in `Test.txt` so that the test script is successful in every commit.
