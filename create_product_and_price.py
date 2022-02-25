# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import stripe, apikey
stripe.api_key = apikey.get()

product = stripe.Product.create(name = "T-shirt")

price = stripe.Price.create(
  product=product.id,
  unit_amount=2000,
  currency='eur',
)

print(price)