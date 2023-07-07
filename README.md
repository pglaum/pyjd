# pyjd

This is a wrapper for the JDownloader API.

## Installation

```shell
pip install pyjd
```

## Usage

The documentation of the JDownloader API can be found here
<https://my.jdownloader.org/developers/>. This library includes all of the
documented functions (but uses underscores instead of CamelCase).

For examples, check out the sample scripts in the repository
([see here](https://github.com/pglaum/pyjd/tree/master/examples)).

## Building auto-docs

### Build

Go to into the `docs` directory and run `make html`.

You can remove the `docs/_build` directory to make a clean rebuild.

### Reload modules

Run `sphinx-apidoc -o source ../` inside the `docs` directory.
Then, remove the `setup.rst` file from the source folder.

## Credits

The MyJD API authentication code is taken from here:
<https://github.com/mmarquezs/My.Jdownloader-API-Python-Library>
