

def generate_random_email():
    import random
    import string

    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    domain = 'mail.com'
    return f"{username}@{domain}"



