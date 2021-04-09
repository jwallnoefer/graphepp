# Contributing to GraphEPP

Code Contributions to GraphEPP should be made on on their own Git
branches via a pull request to its `dev` branch. The pull request will
first be reviewed and merged to `dev` and, after further evaluation,
propagated to the `main` branch from where it can be included into
an official release.

## Development Environment

You can setup a development Environment for GraphEPP like so:

```
git clone https://github.com/jwallnoefer/graphepp.git
cd graphepp
python -m venv eppenv && source eppenv/bin/activate
git checkout -b "$USER-branch"
pip install -r requirements-dev.txt
pre-commit install
```

Which should clone this repository and install the necessary tools and
dependencies into a Python virtual environment named `eppenv`.
You can enter this environment by via `source eppenv/bin/activate`
(on windows: `eppenv\Scripts\activate.bat`) and exit it by calling
`deactivate`.

## Workflows

The GraphEPP repository on Github has number of workflows
(Github Actions) for automatic checking, packaging and releasing of
our Code.

 * Any commit to the repository will be subjected to code quality checks
   using [pre-commit](https://pre-commit.com/). This helps mitigate
   formatting disputes and common mistakes.
 * Any commit will be packages and uploaded to the test index as
   https://test.pypi.org/project/graphepp/ for development convenience.
   From there it can be installed with:
   ```
   pip install --pre -i https://test.pypi.org/simple/ graphepp
   ```
 * Any pull request will cause the unit tests in `./tests/` to be
   executed.
 * A push to the `main` branch will trigger the same checks as a pull
   request.
 * A push of a new version tag to `main` will trigger the same checks
   as a pull request would and cause the new version to be uploaded to the
   main Python Package Index at https://pypi.org/project/graphepp/

If you have set up your development environment as described above,
the code quality checks should run at every local commit.
You can run them manually with:

```
pre-commit run --all-files
```

Skip individual checks with:

```
env SKIP=black,check-ast git commit -m 'some message'
```

Or skip the local checks alltogether:

```
git commit --no-verify -m 'some message'
```

## Tests

We strongly encourage you to write tests and run them locally prior to
any push to the Github repository.
Tests are located in the `./tests/` directory and we use [pytest](https://docs.pytest.org/en/stable/)
as our testrunner.

The most common way to invoke pytest is by running:

```
pytest --log-level=DEBUG --log-cli-level=DEBUG --show-capture=all --maxfail 1 -k "equivalence or noisy"
```

in your development environment.

Some of the most common pytest options are:

 * `-maxfail <number>` stop after a number of failed tests
 * `--pdb` start a pdb debugger session where a test case failed
 * `-k <erpressions>` to run only cases with matching names or classes (partial matches are fine)
 * `-m <markers>` to run only marked tests (`pytest --markers` to show possible markers to mark cases with)

Logical operators like `not`, `and` and `or` can be used with markers and expressions.
You can run exclusively those tests in individual files by passing their paths as
arguments:

```
pytest ./tests/graphepp_test.py
```

But pytest is very good at auto-discovery.

## Packaging

Packages can be manually build and uploaded with:

```
rm -rf ./dist/
python setup.py bdist_wheel
twine upload ./dist/raphepp-*.whl \
    --username __token__ --password "$(pass graphepp-pypi-token)" \
    --repository-url https://test.pypi.org/legacy/
```

Where the `--repository-url` can be omitted for the main Python Package
Index. We strongly recommend using a password manager like `pass` in
the example or twine's configuration file to manage the authentication token.