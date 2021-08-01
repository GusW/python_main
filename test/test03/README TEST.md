# gustavo.watanabe@gmail.com

## Setting up your environment

You will need:

- Python 3.6 or superior
- [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/).
- Operating system: Linux or MacOSX (no support for windows)

### Setup commands & Ensure dependencies

$ virtualenv -p /usr/bin/python3.6 venv
$ source venv/bin/activate
(venv)$ sudo make dependencies

First time running make tests:
(venv)$ sudo make tests

First time running make tests:
(venv)$ sudo make tests

Running the server:
(venv)$ make run

You may need to export PYTHONPATH if running into ImportError on running the server:
$ export PYTHONPATH="${PYTHONPATH}:/path/to/application"

####

## Thank you!
