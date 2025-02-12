import random

def generate_name(name_type="first"):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    name = ''
    
    # Configure parameters based on name type
    if name_type == "first":
        min_syllables = 2
        max_syllables = 3
        final_consonant_chance = 0.3
    else:  # last name
        min_syllables = 2
        max_syllables = 4
        final_consonant_chance = 0.6
    
    syllables = random.randint(min_syllables, max_syllables)
    
    # Build name with consonant-vowel pairs
    for _ in range(syllables):
        name += random.choice(consonants) + random.choice(vowels)
    
    # Add optional final consonant
    if random.random() < final_consonant_chance:
        name += random.choice(consonants)
    
    # Occasionally add a second consonant for last names
    if name_type == "last" and random.random() < 0.2:
        name += random.choice(consonants)
    
    return name.capitalize()

def generate_full_names(num_names=10):
    return [f"{generate_name('first')} {generate_name('last')}" for _ in range(num_names)]

# Generate and print 10 full names
full_names = generate_full_names()
for name in full_names:
    print(name)