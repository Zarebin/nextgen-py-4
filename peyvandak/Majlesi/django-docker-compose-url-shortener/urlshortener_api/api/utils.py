'''
Utilities for Shortner
'''
from django.conf import settings
from random import choice
from string import ascii_letters, digits
import random

SIZE = getattr(settings, 'MAXIMUM_URL_CHARS', 7)
length = 1

AVAILABLE_CHARS = ascii_letters + digits

def create_random_code(chars=AVAILABLE_CHARS):
    """
    Create a random string with the predetermined size
    """
    size_ = random.randint(1, SIZE)
    #size_ = length
    return "".join(
        [choice(chars) for _ in range(size_)]
    )


def create_shortened_url(model_instance):
    random_code = create_random_code()
    print(f"random code", random_code)
    model_class = model_instance.__class__

    if model_class.objects.filter(short_url=random_code).exists():
        return create_shortened_url(model_instance)
    
    return random_code
