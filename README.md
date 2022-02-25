# Accept a Payment with Stripe Checkout

Stripe Checkout is the fastest way to get started with payments. Included are some basic build and run scripts you can use to start up the application.

## Prerequisites

This demo uses
* `pyenv` for Python version managment
* `pipenv` for dependency managment

## Running the sample

1. If you don't have `pyenv` active (e.g. `eval "$(pyenv init -)"` in your rc file) in your shell activate the appropriate Python version via 

~~~
pyenv local 3.9.7
~~~

2. Activate the pipenv environment

~~~
pipenv shell
~~~

3. Build the server

~~~
pip3 install -r requirements.txt
~~~

4. Run the server

~~~
export FLASK_APP=server.py
python3 -m flask run --port=4242
~~~

5. Go to [http://localhost:4242/checkout.html](http://localhost:4242/checkout.html)