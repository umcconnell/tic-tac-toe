# tic-tac-toe

An overengineered, underdesigned, unbeatable tic-tac-toe game.

![Docs](https://github.com/umcconnell/tic-tac-toe/workflows/Docs/badge.svg)

## Table of Contents

-   [Getting Started](#getting-started)
    -   [Prerequisites](#prerequisites)
    -   [Initial setup](#initial-setup)
-   [Distributing](#distributing)
    -   [Installing](#installing)
    -   [Installing additional packages](#installing-additional-packages)
-   [Contributing](#contributing)
-   [Versioning](#versioning)
-   [Authors](#authors)
-   [License](#license)
-   [See also](#see-also)
-   [Acknowledgments](#acknowledgments)

## Getting Started

These instructions will get you a copy of the project up and running on your
local machine for development and testing purposes.

### Prerequisites

You will need python3 and pip3 installed on your machine. You can install it
from the official website https://www.python.org/.

### Initial setup

A step by step series of examples that tell you how to get a virtual python
environment running:

Clone the git repository and navigate into the folder:

```bash
git clone https://github.com/umcconnell/tic-tac-toe.git
cd tic-tac-toe/
```

Then create your virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

To exit the virtual environment run

```bash
deactivate
```

Next, install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Finally, start the app:

```bash
python main.py
# To play against an unbeatable AI, run:
# python main.py --ai minimax
```

Happy coding!

## Distributing

### Installing

To get started, activate the virtual environment:

```bash
source venv/bin/activate
```

Install the packages from `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

### Installing additional packages

After activating the virtual environment, install your package(s):

```bash
python -m pip install <package>
```

Then freeze your packages:

```bash
python -m pip freeze > requirements.txt
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) and
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details on our code of conduct, and
the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available,
see the [tags on this repository](https://github.com/umcconnell/tic-tac-toe/tags).

## Authors

Ulysse McConnell - [umcconnell](https://github.com/umcconnell/)

See also the list of
[contributors](https://github.com/umcconnell/tic-tac-toe/contributors)
who participated in this project.

## License

This project is licensed under the MIT License - see the
[LICENSE.md](LICENSE.md) file for details.

## See also

Check out the great project, including explanatory video, from Dan Shiffman on
The Coding Train about the MiniMax algorithm:
https://thecodingtrain.com/CodingChallenges/154-tic-tac-toe-minimax.html

For a thorough explanation and walk-through of the Minimax algorithm, make sure
to look at [this video](https://www.youtube.com/watch?v=l-hh51ncgDI) from
Sebastian Lague.

Also, look at the great official
[python 3 tutorial](https://docs.python.org/3/tutorial) and especially
[chapter 12](https://docs.python.org/3/tutorial/venv.html) about virtual
environments.

## Acknowledgments

-   [numpy gitignore](https://github.com/numpy/numpy/blob/master/.gitignore) -
    Gitignore inspiration
-   [github python gitignore template](https://github.com/github/gitignore/blob/master/Python.gitignore) - The gitignore template
-   [python3 tutorial](https://docs.python.org/3/tutorial/venv.html) - Guide and
    explanations
-   [VirtualEnv](https://gist.github.com/raulqf/2ca75d7fef2824f03de9761b99b59371) -
    Guide and explanations
-   [python-virtual-environment-howto](https://gist.github.com/simonw/4835a22c79a8d3c29dd155c716b19e16) - Guide and explanations
-   [Contributor Covenant](https://www.contributor-covenant.org/) - Code of Conduct
-   [YT: Sebastion Lague - Algorithms Explained – minimax and alpha-beta pruning](https://www.youtube.com/watch?v=l-hh51ncgDI)
-   [The Coding Train - Tic Tac Toe AI with Minimax Algorithm](https://thecodingtrain.com/CodingChallenges/154-tic-tac-toe-minimax.html)
