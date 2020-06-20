# SDE Online Assessment

This git repository receives an input JSON file which will define an array of bond objects (corporate or government). The output contains the JSON file which includes the corporate bond corresponding to government bond and the spread between both the bonds.

## Running Instructions -
`bash sde_test_solution.sh <sample_input.json> <sample_output.json> `

#### Example -

`bash sde_test_solution.sh test_files/sample_input.json sample_output.json`

## Environment
- Dockerfile specifies instructions for the environment
- Python version used is 3.7
- Pipenv is used for python package management
- Packages installed our specified in Pipfile

## Test cases
- test_files inside submission directory contains input and output test files
- Test Case 1 - Same as given input
- Test Case 2 - If a govt bond is matched to a corp bond, they should not be used again
- Test Case 3 - Fail if values is missing
- Test Case 4 - bps value should be absolute and not negative



