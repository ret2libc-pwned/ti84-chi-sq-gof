import math
import random

SIMULATIONS = int(1e4)

def chi_square_statistic(num_of_vars, obs, exp):
    return sum((obs[i] - exp[i]) ** 2 / exp[i] for i in range(num_of_vars))

def chi_square_p_value(chi_sq, num_of_vars, exp, simulations=SIMULATIONS):
    count = 0
    for _ in range(simulations):
        simulated_obs = [random.uniform(0, 2 * exp[i]) for i in range(num_of_vars)]
        simulated_chi_sq = sum((simulated_obs[i] - exp[i]) ** 2 / exp[i] for i in range(num_of_vars))
        if simulated_chi_sq >= chi_sq:
            count += 1
    return count / simulations

num_of_vars = int(input("Input # of variables: "))
Obs = []
Exp = []

print("Now input the Obs vector...")
for i in range(num_of_vars):
    Obs.append(float(eval(input("\tObs[" + str(i + 1) + "] = "))))

print("Now input the Exp vector...")
for i in range(num_of_vars):
    Exp.append(float(eval(input("\tExp[" + str(i + 1) + "] = "))))

chi_sq = chi_square_statistic(num_of_vars, Obs, Exp)
print("Chi-Square Statistic: " + str(chi_sq))

p_value = chi_square_p_value(chi_sq, num_of_vars, Exp)
print("Estimated p-value: " + str(p_value))
