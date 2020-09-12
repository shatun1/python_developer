import random, os, sys
def rand_object(objective_massive):
    if objective_massive:
        result = random.choice(objective_massive)
        return result
print(rand_object([1, 2, 3, 4]))

