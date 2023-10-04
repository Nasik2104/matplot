import matplotlib.pyplot as plt
import numpy as np

def get_bar():
    months = ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень']
    sales = [150, 200, 180, 300, 250]
    
    plt.bar(months, sales)
    plt.xlabel('Місяць')
    plt.ylabel('Кількість продаж')
    plt.title('Продаж за місяць')

    plt.show()
# get_bar()

def get_plot():
    my_list_x = np.arange(-11, 11, 0.01)
    my_list_y = np.sinc(my_list_x)
    print(my_list_x, my_list_y)
    plt.plot(my_list_x, my_list_y)
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.title('Лінійний графік')
    plt.show()

# get_plot()

def get_plot_customized():
    my_list_x = list(range(100))
    my_list_y = [2^point for point in range(100)]

    plt.plot(my_list_x, my_list_y, marker='o', linestyle='dashed', color='b', label='Dashed graph')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.title('Dashed graph test')
    plt.legend()
    plt.show()

# get_plot_customized()

def get_plot_customized_with_grid():
    plt.grid(True)
    get_plot_customized()

# get_plot_customized_with_grid()

def get_subplots():
    x = list(range(5))
    y_2 = [0, 1, 4, 9, 16]
    y_3 = [0, 1, 8, 27, 64]

    plt.subplot(1, 2, 1)
    plt.plot(x, y_2)
    plt.title('y = x^2')

    plt.subplot(1, 2, 2)
    plt.plot(x, y_3)
    plt.title('y = x^3')

    plt.tight_layout()
    plt.show()


# get_subplots()

def get_scatter():
    x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
    y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
    # colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
    # plt.scatter(x, y, c=colors)

    # colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
    # plt.scatter(x, y, c=colors, cmap='viridis')
    # plt.colorbar()

    # sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
    # plt.scatter(x, y, s=sizes, alpha=0.5)

    # x = np.array([5,2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
    # y = np.array([99,100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
    # plt.scatter(x, y, color='#50af5d')

    x = np.random.randint(100, size=(100))
    y = np.random.randint(100, size=(100))
    colors = np.random.randint(100, size=(100))
    sizes = 10 * np.random.randint(100, size=(100))

    plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='gist_rainbow')
    plt.colorbar()

    plt.show()

get_scatter()
