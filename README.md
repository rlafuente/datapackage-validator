# dpkg-validate

This is a simple wrapper script to validate data packages in the command line. It uses the excellent [datapackage-validate-py](https://github.com/okfn/datapackage-validate-py/) library to do all the work.

## Installation

Run `make install`. A virtualenv with all necessary dependencies will be created in the project directory.

## Usage

Be sure to load the virtualenv before running the script. This is done after installation, but if you are opening a new shell or terminal, you need to activate the virtualenv prior to running `dpkg-validate.py`:

    source .env/bin/activate

After this, to run the script just indicate the location of the data package -- either a `datapackage.json` file or a directory containing one:

    python dpkg-validate.py ~/datasets/cpi
    # or pointing to the file itself
    python dpkg-validate.py ~/datasets/cpi/datapackage.json

If the JSON file is fine, there will be no output. Otherwise, a list with the errors will be printed to standard output.
