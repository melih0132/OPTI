# Fonction qualité en fonction de la température
def quality(temp):
    return - (temp - 200)**2 + 100

# Descente de gradient pour trouver la température optimale
current_temp = 190  # Point de départ
learning_rate = 1   # Taille des pas
precision = 0.01    # Seuil de précision
max_iterations = 1000
iteration = 0

while True:
    # Calculer le gradient (pente)
    gradient = -2 * (current_temp - 200)
    
    # Ajuster la température
    new_temp = current_temp + learning_rate * gradient
    
    # Arrêter si la différence est très petite
    if abs(new_temp - current_temp) < precision:
        break
    
    current_temp = new_temp
    iteration += 1
    if iteration > max_iterations:
        break

print(f"Température optimale trouvée : {current_temp:.2f}°C après {iteration} itérations.")
