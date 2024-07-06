from faker import Faker

# Create a faker isntance
fake = Faker()

#Generate a fake name
print(fake.name())
# Output might be something like: "John Doe"

#Generate a fake address
print(fake.address())