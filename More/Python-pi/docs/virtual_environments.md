# Python virtual environments

## Create a new environment

```commandline
$ python -m venv .venv
```

* The name ``.venv`` is only a convention.
* The virtual environment (with relative path) is created in the current directory.
* The ``python`` command maybe ``python3`` or similar on your system.

## Activate the environment

On windows systems you can activate the virtual environment by using the following command.
```commandline
$ .venv\Scripts\activate.bat
```

## Install packages

As an example you can install Jupyter notebook by the following command.
```commandline
(.venv) pip install jupyter
```

After, you can start the notebook by
```commandline
(.venv) jupyter notebook
```
