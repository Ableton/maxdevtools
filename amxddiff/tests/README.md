# Testing

The tests allow us to make sure we didn't accidentally change something to the patch printing script that changes its output in an unintended way.

## Running the tests

From the `amxddiff` folder, run `python3 tests/test.py`

## Changing the script

Whenever adding something to the patch printer script, ideally this new case is included in the `Test.amxd` device. After checking that the resulting patch summary differs only in the expected way, the new result from the script should then be saved as `Test.txt`.

Every commit to this repository that changes the output of the scripts should be accompanied by a change in `Test.txt` so that the test script is successful in every commit. Note that `Test.txt` should always end with a new line.
