from faker import Faker

def generate_email():
    fake = Faker("en_US")

    return fake.free_email()
