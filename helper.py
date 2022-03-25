import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

def define_city(ncity = 100, area = [100,100], SEED = 161):
    """Create a dictionay with the random location of cities in the specified area """
    cities_dict = {}
    np.random.seed(SEED)
    city_arr_x = np.array(range(ncity))
    city_arr_y = np.array(range(ncity))
    np.random.shuffle(city_arr_x)
    np.random.shuffle(city_arr_y)
    cities = pd.DataFrame({'X':city_arr_x , 'Y':city_arr_y}, index=range(ncity))
    return cities

def print_map(city_map):
    for index, row in city_map.iterrows():
        plt.plot(row['X'],row['Y'], 'ro')
    
    plt.title('City location')
    plt.show()  

def print_path(path, city_map):
    for index, row in city_map.iterrows():
        plt.plot(row['X'],row['Y'], 'ro')

    X = []
    Y = []
    for index in path: 
        X.append(city_map.iloc[index].X)
        Y.append(city_map.iloc[index].Y)
    
    plt.plot(X,Y)
    plt.title('Travel path')
    plt.show()  


def distance(city1, city2):
    distan = 0
    #print(city1['X'], city1['Y'])
    X_dist = (city2['X']-city1['X'])**2
    Y_dist = (city2['Y']-city1['Y'])**2
    distan = math.sqrt((X_dist + Y_dist))
    return distan

def fitness(population, cities):
    dist = 0
    vec = []
    for index, chromosome in population.iterrows():
        for i in range(len(chromosome)-1):
            dist = dist + distance(cities.iloc[chromosome[i]], cities.iloc[chromosome[i+1]])
        dist = dist + distance(cities.iloc[chromosome[len(chromosome)-1]], cities.iloc[chromosome[0]])
        vec.append(dist)
        dist = 0
    return vec


def generate_population(individuals, genes = 100, population = 100, gene_value = 100):
    pop = {}
    for ind in range(5*population):
        pop[ind] = np.random.randint(gene_value, size = genes)

    pop_df = pd.DataFrame.from_dict(pop, orient='index')
    fit = fitness(pop_df, individuals)
    pop_df["fit"] = fit
    pop_df = pop_df.sort_values(by=['fit'], ascending=True)
    pop_df = pop_df.iloc[:population]
    return pop_df

def mutation(chromosome):
    size = len(chromosome) - 1 # remove one due fit column
    changes = np.random.randint(size, size = 2)
    chromosome[changes[0]], chromosome[changes[1]] = chromosome[changes[1]], chromosome[changes[0]] 
    return chromosome

def cross_over(chromo1, chromo2):
    size = len(chromo1) - 1 # remove one due fit column
    index = np.random.randint(size)
    #print("Index: ", index)
    #print("Len of chromosome initial: ", len(chromo1), len(np.unique(chromo1, axis=0)))
    #print("Len of chromosome 2 initial: ", len(chromo2), len(np.unique(chromo2 ,axis=0)))
    #print("Index: ",index)
    chr1 = chromo1[:index]
    chr2 = chromo2[:index]
    chromo1[:index], chromo2[:index] = chr2, chr1
    
    chromo1 = np.unique(chromo1,axis = 0)
    chromo2 = np.unique(chromo2, axis = 0)

    miss1 = []
    miss2 = []

    for number in range(size):
        if not (number in chromo1):
            miss1.append(number)
    for number in range(size):
        if not (number in chromo2):
             miss2.append(number)
             
    #print("missing 1: ", miss1)
    #print("missing 2: ", miss2)

    
    chromo1 = np.append(chromo1, np.array(miss1))
    chromo2 = np.append(chromo2, np.array(miss2))
    #print("Chromossome1: ", chromo1.shape)
    return chromo1, chromo2


def select_partner(gene, index):
    selected = random.sample(range(gene), 2)

    for value in selected:
        if value != index:
            #print("Partner Index: ", value)
            return value
    
    
            

    


