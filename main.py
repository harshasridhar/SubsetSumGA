import numpy as np 
import math
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
n = 5
sum = 35
data = [1,2,3,4,5,6,7,8,9,10]
population = []
for i in range(n):
    population.append({"chromosome" :np.random.randint(2,size = len(data)), "fitness" : 0})
    population[i]["fitness"] = fitness(population[i]['chromosome'],data,sum)
print('Required Sum : '+str(sum))
for i in range(n):
    print(population[i])