import random
import string

url = "https://qa-desk.education-services.ru"

user = "".join(random.choices(string.ascii_lowercase, k=10))
domain = "".join(random.choices(string.ascii_lowercase, k=5))
random_email = f"{user}@{domain}.com"

email_without_mask = "".join(random.choices(string.ascii_lowercase, k=5))

password = "password"

test_user = "shevelkov_33_test_user@mail.com"
