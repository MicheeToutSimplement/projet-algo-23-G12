from Q1 import *
# Calcul des énergies cinétique, potentielle et mécanique pour le cas a)

E_cinetique_a = 0.5 * m * x_a[:, 1]**2
E_potentielle_a = 0.5 * k * x_a[:, 0]**2
E_mecanique_a = E_cinetique_a + E_potentielle_a

# Plot de l'Ep, l'Ec et l'Em

plt.figure()
plt.plot(t_a, E_cinetique_a, label='Energie cinétique')
plt.plot(t_a, E_potentielle_a, label='Energie potentielle')
plt.plot(t_a, E_mecanique_a, label='Energie mécanique')
plt.xlabel('Temps (s)')
plt.ylabel('Ec, Ep et Em (J)')
plt.legend()
plt.title('Ec, Ep et Em à tout instant')
plt.show()
