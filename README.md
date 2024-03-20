# CImaging Python Library Template

## Architecture

```
├── .github                     -> Github setup
│   └── workflows
│       └── ci_pipeline.yml     -> Prepared CI pipeline to run tests, build the library and publish it
├── .pre-commit-config.yaml     -> Pre-commit configuration with standard options
├── cimaging_python_template    -> Your library code-base
│   └── [...].py
├── CHANGELOG.md                -> Changelog skeleton
├── README.md                   -> This Readme file
├── pyproject.toml              -> Python/Poetry basic configuration
├── poetry.lock                 -> Poetry stored state
└── tests
    └── unit                    -> Unit tests folder
        └── test_[...].py       -> Your unit-testing code-base
```

## Usage

Poetry is used for most operations. You should have it available on your setup to run most commands. (`pip(x) install poetry`)

### Install dependencies

You can install the dependencies using `poetry install`. This will install the dependencies state which is in `poetry.lock`.

You can update the locked versions using `poetry update`.

### Add dependency

You can add new dependencies using `poetry add [package][@version-constraint]`.
Doing it that way, Poetry will try to get a proper version of this package, matching your existing setup.
If you want to recompute every versions to avoid conflicts, you may want to add the dependencies in the `[tool.poetry.dependencies]` section.

As a library, only the main dependencies will be communicated to the packages which will depend on it. As such, please make sure you're not too restrictive with the versions you set.
If you don't specify versions, it'll try to get the latest available and compatible one.

### Add dev dependency

You can add new dev dependencies using the same command as above but adding `--group=dev`.

Please note that any dependencies added to `dev` group won't be passed to projects depending on your library.

### Run linting

You can run the different linters using `poetry run [black/pylint/isort/mypy]` with potentially some additional arguments.
The different linters are also added to the pre-commit hook, so you can run them using `pre-commit run [--all-files]`.

### Run tests

You can run your tests using `poetry run pytest`.

### Build & publish library

You can build your library using `poetry build`. You can also publish your library using `poetry publish --repository=prophesee`.
To do so you need to have setup the remote repository (should be done only once): `poetry config repositories.prophesee [pypi repository URI]`

Publishing should only be done using the CI however.

## Initialize your project

To bootstrap your project, what you should do:

1. Create a repo on GitHub using this one as its template
2. Change the name of the Poetry project in `pyproject.toml`
3. Rename the `cimaging_python_template` folder to match your library name (using `_` instead of `-`)
4. Adapt this Readme accordingly.
5. Run `pre-commit install`
6. Update the SonarQube configuration in `.github/workflows/ci_pipeline.yml` and uncomment the SonarQube steps
7. Run `poetry update`
8. Enjoy your fresh setup
