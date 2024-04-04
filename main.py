import numpy as np
import csv
import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
import random
import time


#task1
def listscount():
    list1 = [random.randint(0, 1000) for i in range(1000000)]
    list2 = [random.randint(0, 1000) for i in range(1000000)]
    time_start = time.perf_counter()
    [a * b for a, b in zip(list1, list2)]
    time_end = time.perf_counter()
    time_lists = time_end - time_start
    return time_lists


def arrayscount():    
    array1 = np.random.randint(0, 1000, 10000000)
    array2 = np.random.randint(0, 1000, 10000000)
    time_start_numpy = time.perf_counter()
    np.multiply(array1, array2)
    time_end_numpy = time.perf_counter()
    return time_end_numpy - time_start_numpy


def task1():
    print ('Время выполнения списков:', listscount())
    print ('Время выполнения массивов:', arrayscount())
    print('Numpy быстрее списка в ', (listscount())/(arrayscount()), ' раз')




#task2
def task2():

    with open('data1.csv', newline='', ) as f:
        data = []
        a = csv.reader(f, delimiter=';')
        for i in a:
            data.append(i)

    def col1():
        column1 = []
        for i in range(1, len(data)):
            column1.append(data[i][0])
        time = [float(x) for x in column1]
        return time

    def col10():
        column10 = []
        for i in range(1, len(data)):
            column10.append(data[i][9])
        angle_ignition = [float(x) for x in column10]
        return angle_ignition

    def col16():
        column16 = []
        for i in range(1, len(data)):
            column16.append(data[i][15])
        air_consumption = [float(x) for x in column16]
        return air_consumption


    def correlation():
        correl = []
        for i in range(len(col10())):
            correl.append(float((col10()[i]+col16()[i])/2))
        return correl


    plt.plot(col1(), col10(), label='10-column plot')
    plt.plot(col1(), col16(), label='16-column plot')
    plt.plot(col1(), correlation(), label='average')
    plt.xlabel('1 column')
    plt.ylabel('10 and 16 column')
    plt.legend()
    plt.show()

#task3
def task3():
    x = np.linspace(-5*np.pi, 5*np.pi, 20)
    y = np.linspace(-5*np.pi, 5*np.pi, 20)
    z = y*np.cos(x)
    
    ax = plt.axes(projection='3d')
    ax.plot(x, y, z)

    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.set_zlabel('z', fontsize=12)
    ax.set_title('x∈(-5п;5п); y∈(-5п;5п); z=y cos(x)')
    plt.show()

if __name__ == '__main__':
    # task1()
    # task2()
    task3()
