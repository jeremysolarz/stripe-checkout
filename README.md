# Accept a Payment with Stripe Checkout

Stripe Checkout is the fastest way to get started with payments. Included are some basic build and run scripts you can use to start up the application.

## Prerequisites

This demo uses
* `pyenv` for Python version managment
* `pipenv` for dependency managment

1. Create a customer

~~~
python create_customer.py
~~~

Copy or replace the existing value for `customer=` with the generated key 
starting with *cus_* into `server.py` into the call of `stripe.checkout.Session.create`

1. Create a product and price for it

~~~
python create_product_and_price.py
~~~

Copy or replace the existing value for `price=` with the generated key 
starting with *price_* into `server.py`
into the call of `stripe.checkout.Session.create`

## Running the sample

1. If you don't have `pyenv` active (e.g. `eval "$(pyenv init -)"` in your rc file) in your shell activate the appropriate Python version via 

~~~
pyenv local 3.9.7
~~~

2. Activate the pipenv environment

~~~
pipenv shell
~~~

3. Install dependencies

~~~
pipenv install
~~~

4. Run the server

~~~
export FLASK_APP=server.py
python3 -m flask run --port=4242
~~~

5. Go to [http://localhost:4242/checkout.html](http://localhost:4242/checkout.html)

6. Test with different cards ([test cards](https://stripe.com/docs/testing))
* No SCA: 4242424242424242
* SCA: 4000056655665556