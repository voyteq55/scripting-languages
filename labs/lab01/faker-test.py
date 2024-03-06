from faker import Faker
fake = Faker()
for _ in range(10):
    print(fake.name())