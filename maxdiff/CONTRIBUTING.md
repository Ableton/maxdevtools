# Contributing to maxdiff

This tool is an on-going work in progress, issue reports and ideas for adaptations are very welcome.

## Reporting issues

If you have a Max patch or device that results in an error or is not represented as you would expect, please [create an issue on github](https://github.com/Ableton/maxdevtools/issues) and include the patch that doesn't work plus a description of the problem you're seeing.

## Pull requests

We are happy to accept pull requests from the GitHub community, assuming that they meet the guidelines below.

### We have a signed Contributor License Agreement

You have signed and returned Ableton's [CLA](http://ableton.github.io/cla/).

### Code formatting

Code is formatted using black:
* Install [black](https://pypi.org/project/black/)
* Run `black .` in the repo root

Black formatting will be checked as a GitHub action for Pull Requests.

### Typing and using mypy in development

This codebase uses the optional [typing](https://docs.python.org/3/library/typing.html) available in Python. This makes it so other tooling such as [mypy](https://mypy-lang.org/) can statically analyse your code for errors before you've even run a test. This synergy of types and tooling is useful in an automated context and for doing holistic evaluation, but also the types themselves can provide useful information to people reading and extending the codebase.

[mypy](https://mypy-lang.org/) is relatively easy to setup with its [getting started](https://mypy.readthedocs.io/en/stable/getting_started.html) instructions. Once setup, you can check `maxdiff` as a whole project for type issues by running `mypy maxdiff` from the root of this monorepo, or `mypy .` if your current working directory is already set to the `maxdiff` project.

### Testing

Whenever making a change, we test that the previous functionality still works as before. For more info, see the [tests](tests/) folder.

These tests will run as a GitHub action for Pull Requests.