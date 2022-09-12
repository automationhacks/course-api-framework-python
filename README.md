# Building an API test automation framework with Python

## Purpose

Code for TAU (Test automation university) course on building an API framework with Python. Once
ready this would be published at
[Test automation university](https://testautomationu.applitools.com/), You can also find a series of
blogs that I'm writing for this course on my blog
[https://automationhacks.io/](https://automationhacks.io/tags/) under `Python` tag. However, the
video courses are going to have much more context and in depth discussions

## Setup

Ensure you have
[pipenv already installed](https://automationhacks.io/2020/07/12/how-to-manage-your-python-virtualenvs-with-pipenv/):

```zsh
# Activate virtualenv
pipenv shell
# Install all dependencies in your virtualenv
pipenv install
```

## How to navigate

Each chapter has its own dedicated branch in `/example/<chapter_no>_<topic>` format. For e.g.
`example/01_setup_python_dependencies`

You can either use your IDE or terminal to switch to that branch and see the last updated commit.

```zsh
# Checkout the entire branch
git checkout example/01_setup_python_dependencies
# Checkout to a specific commit, here <sha> can be found using `git log` command
git checkout <sha>
```

## Application under test

This automated test suite covers features of `people-api`, Please refer the Github repo
[here](https://github.com/automationhacks/people-api).

Note: These tests expect the `people-api` and `covid-tracker` API to be up. You would find
instructions in the `people-api` repo

## How to run

```zsh
# Setup report portal on docker
# Update rp_uuid in pytest.ini with project token
docker-compose -f docker-compose.yml -p reportportal up -d

# Launch pipenv
pipenv shell

# Install all packages
pipenv install

# Run tests via pytest (single threaded)
python -m pytest

# Run tests in parallel
python -m pytest -n auto

# Report results to report portal
python -m pytest -n auto ./tests --reportportal
```

## Discuss?

Feel free to use the
[Github discussions](https://github.com/automationhacks/course-api-framework-python/discussions/1)
in this repo to ✍🏼 your thoughts or even use the disqus comments section on the blogs.

Happy learning!
