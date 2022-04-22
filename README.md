# RateThisPad

*WARNING* Instructions are out of date! Use podman!

## Setup Instructions

- Purge and minify CSS
  - npm i -g purgecss minify
  - ./scripts/css-purge-and-minify.sh

- To get local scripts (runserver.sh, etc) working, add environment variables for virtualenv:
  - Copy the template in ./scripts/venv-scripts/postactivate.default to postactivate and assign any desired environment variables there
  - Symlink your postactivate script to /[venv-dir]/bin/postactivate

- Create a new virtualenv
  - If virtualenvwrapper not installed, install it now
  - mkvirtualenv your-venv

- Install packages
  - dev
    - poetry install
  - production
    - poetry install --no-dev

- Run the migrations
  - python3 manage.py migrate

- Consolidate static files
  - python3 manage.py collectstatic
