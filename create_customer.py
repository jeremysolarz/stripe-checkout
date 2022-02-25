import stripe, apikey
stripe.api_key = apikey.get()

customer = stripe.Customer.create(
  description="My First Test Customer (created for API docs)",
)

print(customer)