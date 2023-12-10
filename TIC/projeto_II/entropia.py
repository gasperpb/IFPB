import math

def calculate_entropy(probabilities):
    entropy = 0
    for p in probabilities:
        if p > 0:
            entropy += -p * math.log2(p)
    return entropy

# Exemplo de probabilidades
probabilities = [0.5, 0.5]  # Probabilidades pelos valores desejados

entropy = calculate_entropy(probabilities)
print("Entropia do conjunto:", entropy)
