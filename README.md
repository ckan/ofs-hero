# ofs-hero
Rescues broken filestores because ofs is not thread-safe. This script generates
the minimal JSON that's required for the filestore to work. Pull requests
welcome to make it more closer to the original JSON.

## Instructions
After activating your virtualenv, `cd` to the `src` directory, install the
sources via pip::

    $ (default) pip install -e git+git://github.com/ckan/ofs-hero.git#egg=ofs_hero

Install the requirements::

    $ (default) pip install -r ofs-hero/pip-requirements.txt

## Usage
Switch to the `ofs-hero` directory and run the paster command pointint to the
config file::

    $ (default) paster regenerate -c /etc/ckan/default/production.ini

This will print the JSON value. Pipe it to a file and replace the
`persisted_state.json` file in the flestore::

    $ (default) paster regenerate -c /etc/ckan/default/production.ini > persisted_state.json

It is recommended that you shutdown the webserver before replacing the file.
