# dpkg-validate

This is a simple wrapper script to validate data packages in the command line. It uses the excellent [datapackage-validate-py](https://github.com/okfn/datapackage-validate-py/) library to do all the work.

## Usage

Just indicate the location of the data package -- either a `datapackage.json` file or a directory containing one:

    python dpkg-validate.py ~/datasets/cpi
    # or pointing to the file itself
    python dpkg-validate.py ~/datasets/cpi/datapackage.json
