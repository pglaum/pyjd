# PyJD

This is a wrapper for the JDownloader API.

More information: <https://pglaum.srht.site/pyjd-api>

## Building auto-docs

### Build

Go to into the `docs` directory and run `make html`.

You can remove the `docs/_build` directory to make a clean rebuild.

### Reload modules

Run `sphinx-apidoc -o source ../` inside the `docs` directory.
Then, remove the `setup.rst` file from the source folder.

## Credits

The MyJD API authentication is taken from here:
<https://github.com/mmarquezs/My.Jdownloader-API-Python-Library>
