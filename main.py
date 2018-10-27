import numpy as np 
import math
from operator import itemgetter
import random
solutions = []
def crossover(parent1 , parent2):
    point =5
    child1 = np.concatenate((parent1[:point],parent2[point:]),axis=None)
    child2 = np.concatenate((parent2[:point],parent1[point:]),axis=None)
    return child1,child2
def fitness(array,data,sum):
    c=0
    for i in range(len(data)):
        if(array[i] == 1):
            c += data[i]
    # print('sum :'+ str(c)+"\tDifference :" +str(c-sum))
    if c == sum:
        return 100
    else :
        return (1/abs(c-sum))*100
# limit = input('Enter the max limit: ')
# n = input('Enter the population size: ')
# sum = input('Enter the sum to be obtained: ')
# population = []
# for i in range(n):
n = 20
sum = 35
data = [1,2,3,4,5,6,7,8,9,10]
mutation_rate = 0.2
crossover_rate = 0.4
population = []
for i in range(n):
    population.append({"chromosome" :np.random.randint(2,size = len(data)), "fitness" : 0})
    population[i]["fitness"] = fitness(population[i]['chromosome'],data,sum)
    if(int(population[i]['fitness']) == 100):
        solutions.append(population[i]['chromosome'])
print('Required Sum : '+str(sum))
#sort the population by the fitness values
population = sorted(population, key = itemgetter('fitness'))
for i in range(n):
    print(population[i])

# ranking process
random_values = np.random.rand(n)
random_values = [ i/ random_values.sum() for i in random_values]
random_values.sort()
ranks = np.array(random_values)
ranks = ranks*n
ranks =ranks.round()
print(ranks)

new_population = []
for i in range(len(population)):
    for j in range(int(ranks[i])):
        new_population.append(population[i])
# new population after ranking process
print(new_population)

num_strings_for_crossover = round(len(new_population)*crossover_rate)
num_strings_for_crossover = num_strings_for_crossover+1 if num_strings_for_crossover%2!=0 else num_strings_for_crossover
strings_selected = random.sample(range(0,len(new_population)),num_strings_for_crossover)
print("Number of strings selected : " +str(num_strings_for_crossover))
print(strings_selected)
print( solutions)
#crossover operation
for i in range(int(len(strings_selected)/2)):
    population[i]["chromosome"],population[len(strings_selected)-i]["chromosome"] = crossover(population[i]["chromosome"],population[len(strings_selected)-i]["chromosome"])
