import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import helper


epochs = 20 # number of times the iteration will happen
mut = 0.1 # probability that the mutation happen
cross = 0.6 # probability that cross over happen
ncity = 100
pop = 250

# define cities to be searched 

city = helper.define_city()

# define initial population

population = helper.generate_population(city,100,pop,100)

# print city location 

#helper.print_map(city)

minimal_distance = []
for epoch in range(epochs): 
    for index, chromo in population.iterrows():
        prob = np.random.rand() 
        if prob <= mut:
            chromo = helper.mutation(chromo) # mutation happen
        elif prob <= cross:
            partner_index = helper.select_partner(ncity, index)
            partner = population.iloc[partner_index]
            ch1,ch2 = helper.cross_over(chromo, partner)
            print("index: ", index)
            print("Crossed over 1 ", ch1.shape)
            print("Crossed over 2 ", ch2.shape)
            print("Chromo: ", population.iloc[index].shape)
            print("Partner: ", population.iloc[partner_index].shape)
    population = population.drop(columns= ['fit']) # remove fit column that is not needed
    fit = helper.fitness(population, city) # recalculate fitness
    population['fit'] = fit

    population.sort_values(by=['fit'], ascending=True) # order population by smaller values
    minimal_distance.append(population.iloc[0]['fit'])
    #print(epoch, population.iloc[0]['fit'])

best = population.iloc[0]
min_distance = best['fit']
print("Smaller distance", str(min_distance))
path = population.drop(columns= ['fit'])
print("Best path found is: ", path.values)

helper.print_path(path, city)




