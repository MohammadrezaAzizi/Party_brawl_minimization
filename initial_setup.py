import numpy as np
import torch
import random

first_names = ["Ali", "Zahra", "Reza", "Sara", "Mohammad", "Fatemeh", "Hossein", "Maryam", "Mehdi", "Narges", "Hamed", "Roya"]
last_names = ["Ahmadi", "Hosseini", "Karimi", "Rahimi", "Hashemi", "Ebrahimi", "Moradi", "Mohammadi", "Rostami", "Fazeli", "Hosseinzadeh", "Niknam"]
def generate_random_names(first_names, last_names, n):
    random_names = []
    while len(random_names) < 24:
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        if not f"{first_name} {last_name}" in random_names:
            random_names.append(f"{first_name} {last_name}")
    return random_names

random_names = generate_random_names(first_names, last_names, 24)

hostility_matrix = np.array(shape=[len(random_names),len(random_names)], dtype=np.float8)
print(torch.__version__)