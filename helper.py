
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def define_city(ncity = 100, area = [100,100], SEED = 161):
    """Create a dictionay with the random location of cities in the "specified area """
    cities_dict = {}
    np.random.seed(SEED)
    x = np.random.randint(area[0]+1, size = ncity)
    y = np.random.randint(area[1]+1, size = ncity)

    index = range(100)

    for i in index:
        cities_dict[i] = [x[i], y[i]]

    cities = pd.DataFrame.from_dict(cities_dict, orient='index', columns=['X', 'Y'])
    
    return cities

def print_map(city_map):
    for index, row in city_map.iterrows():
        plt.plot(row['X'],row['Y'], 'o', color = 'red')
    
    plt.title('City location')
    plt.show()  



city_df = define_city()
print_map(city_df)
