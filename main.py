import numpy as np
import math
from math import exp
from operator import itemgetter
import random
solutions = []
def appendSolution(solution):
    if len(solutions) == 0:
        solutions.append(solution)
    else:
        for sol in solutions:
            if(np.array_equiv(np.array(sol),np.array(solution)) == True):
                return
        solutions.append(solution)
        
def crossover(parent1 , parent2):
    point =5
    child1 = np.concatenate((parent1[:point],parent2[point:]),axis=None)
    child2 = np.concatenate((parent2[:point],parent1[point:]),axis=None)
    return np.array(child1),np.array(child2)

def mutation(parent, mask):
    child=[]
    for i in range(len(parent)):
        child.append( parent[i] if mask[i]==1 else int(not parent[i]))
    return np.array(child)

def fitness(array,data,sum):
    c=0
    for i in range(len(data)):
        if(array[i] == 1):
            c += data[i]
#     if c == sum:
#         return 100.0
#     else :
    return exp(-1.0*abs(c-sum))
#     return (1/abs(c-sum))*100
# limit = input('Enter the max limit: ')
# n = input('Enter the population size: ')
# sum = input('Enter the sum to be obtained: ')
# population = []
# for i in range(n):
n = 35
sum = 35
data = [1,2,3,4,5,6,7,8,9,10]
mutation_rate = 0.2
crossover_rate = 0.4
population = []
for i in range(n):
    population.append({"chromosome" :np.random.randint(2,size = len(data)), "fitness" : 0})
    population[i]["fitness"] = fitness(population[i]['chromosome'],data,sum)
    if((population[i]['fitness']) == 1.0):
        appendSolution(population[i]['chromosome'])
#print('Required Sum : '+str(sum))
#sort the population by the fitness values
population = sorted(population, key = itemgetter('fitness'))
# for i in range(n):
    #print(population[i])
# iterations = 15
iter=0
while(len(solutions)!=31):
# for iter in range(iterations):
    iter +=1
    print("Generation: "+str(iter+1))
    # ranking process
    random_values = np.random.rand(n)
    random_values = [ i/ random_values.sum() for i in random_values]
    random_values.sort()
    ranks = np.array(random_values)
    ranks = ranks*n
    ranks =ranks.round()
    #print(ranks)

    new_population = []
    for i in range(len(population)):
        for j in range(int(ranks[i])):
            new_population.append(population[i])
    # new population after ranking process
    #print(new_population)

    num_strings_for_crossover = round(len(new_population)*crossover_rate)
    num_strings_for_crossover = num_strings_for_crossover+1 if num_strings_for_crossover%2!=0 else num_strings_for_crossover
    strings_selected = random.sample(range(0,len(new_population)),num_strings_for_crossover)
    #print("Number of strings selected : " +str(num_strings_for_crossover))
    #print(strings_selected)
    #print( solutions)

    #print('\n\n')
    #print(new_population)
    #crossover operation
    for i in range(int(len(strings_selected)/2)):
        new_population[i]["chromosome"],new_population[len(strings_selected)-i]["chromosome"] = crossover(new_population[i]["chromosome"],new_population[len(strings_selected)-i]["chromosome"])
    #print('\n\n')
    for i in range(len(new_population)):
            new_population[i]['fitness']=fitness(new_population[i]['chromosome'],data,sum)
    # #print(new_population)

    # mutation
    number_of_mutants = round(mutation_rate * len(new_population))
    #print(number_of_mutants)
    chromosomes_selected = random.sample(range(0,len(new_population)),number_of_mutants)
    #print(chromosomes_selected)
    mask=np.random.randint(2,size = len(data))
    for i in chromosomes_selected:
            new_population[i]['chromosome']=np.array(mutation(new_population[i]['chromosome'],mask))
            new_population[i]['fitness'] = fitness(new_population[i]['chromosome'],data,sum)
    new_population = sorted(new_population, key = itemgetter('fitness'))
    for i in range(len(new_population)):
            if((new_population[i]['fitness']) == 1.0):
                    print(new_population[i])
                    appendSolution(new_population[i]['chromosome'])
    print(iter," ",len(solutions))
    #print('\n\nNew Population after one iteration\n')   
    # for individual in new_population:
            #print(individual)
    #print('\n\n')
    #print(solutions)
f=open('a.plot',"a")
f.write(str(iter)+"\n")
for sol in solutions:
        print(sol)
print(len(solutions))
sum = np.zeros(len(solutions))
print("\n\n")
for i in range(len(solutions)):
        solution = solutions[i]
        for j in range(len(solution)):
                sum[i] += solution[j]*(j+1)
print(sum)