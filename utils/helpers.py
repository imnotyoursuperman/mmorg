import random

def generate_unique_nickname(race, character_class):
    base_name = race[:3] + character_class[:3]
    random_suffix = random.randint(100, 999)
    return base_name + str(random_suffix)
