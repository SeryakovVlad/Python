#'Introduction to programming':Task 7
#Seryakov Vlad, FB-21
import pandas as pd
import matplotlib.pyplot as plt

def plot_sunspots():
    data = pd.read_csv('sunspots.txt', delimiter='\s+', header=None, names=['Month', 'Sunspots'])   

    plt.plot(data['Month'], data['Sunspots'])
    plt.xlabel('Місяць')
    plt.ylabel('Кількість затемнень')
    plt.title('Кількість сонячних затемнень за місяць')
    plt.show()

def plot_sunspots_first_1000():
    data = pd.read_csv('sunspots.txt', delimiter='\s+', header=None, names=['Month', 'Sunspots'])

    plt.plot(data['Month'][:1000], data['Sunspots'][:1000])
    plt.xlabel('Місяць')
    plt.ylabel('Кількість затемнень')
    plt.title('Кількість сонячних затемнень за місяць (перші 1000 значень)')
    plt.show()

def plot_rolling_average():
    data = pd.read_csv('sunspots.txt', delimiter='\s+', header=None, names=['Month', 'Sunspots'])

    r = 5
    rolling_mean = data['Sunspots'].rolling(window=r).mean()

    fig, ax = plt.subplots()
    ax.plot(data['Month'][:1000], data['Sunspots'][:1000], label='Original Data')
    ax.plot(data['Month'][:1000], rolling_mean[:1000], label='Rolling Mean (r=5)')
    ax.set_xlabel('Місяць')
    ax.set_ylabel('Кількість затемнень')
    ax.set_title('Дані про щомісячні сонячні затемнення')
    ax.legend()
    plt.show()

def plot_combined_sunspots():
    data = pd.read_csv('sunspots.txt', delimiter='\s+', header=None, names=['Month', 'Sunspots'])

    plt.subplot(2,1,1)
    plt.plot(data['Month'][:1000], data['Sunspots'][:1000])
    plt.xlabel('Місяць')
    plt.ylabel('Кількість затемнень')
    plt.title('Кількість сонячних затемнень за місяць (перші 1000 значень)')

    plt.subplot(2,1,2)
    r = 5
    rolling_mean = data['Sunspots'].rolling(window=r).mean()
    plt.plot(data['Month'][:1000], data['Sunspots'][:1000], label='Оригінальні дані')
    plt.plot(data['Month'][:1000], rolling_mean[:1000], label='Ковзне середнє (r=5)')
    plt.xlabel('Місяць')
    plt.ylabel('Кількість затемнень')
    plt.title('Кількість сонячних затемнень за місяць (перші 1000 значень)')
    plt.legend()
    plt.show()

plot_sunspots()
plot_sunspots_first_1000()
plot_rolling_average()
plot_combined_sunspots()