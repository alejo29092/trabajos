import matplotlib.pyplot as plt
import seaborn as sns

"""
this class is used for 2 vars
"""


def graphics_use_for_var_one_var(a):
    """

    :param a: value to graph
    :return: 3 type graph
    """
    type_graphic_1_var = input("""input the mode for the grap: 
                         1: kde
                         2: histograma
                         3: violin
                         type graphic: """)

    if type_graphic_1_var == '1':
        sns.kdeplot(a)
    if type_graphic_1_var == '2':
        sns.histplot(a)
    if type_graphic_1_var == '3':
        sns.violinplot(a)


def graphics_use_for_vars(a, b):
    """

    :param a: value to graph
    :param b: value to graph
    :return: graphs the scatter or inverse
    """
    mode = input("""select the mode of the graphics, between.
                 1 = black
                 0 = white
                 mode: """)

    if mode == '1':
        plt.style.use('dark_background')
    elif mode == '0':
        pass
    type_graphic_2_var = input("""input the mode for the grap:
                                1: graphics inverse
                                2: graphics dispers
                                type grapjic: """)
    if type_graphic_2_var == '1':
        fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

        ax1.set_title('relations  x - y')
        ax1.plot(a, b, 'b')
        ax2.set_title('relation y - x')
        ax2.plot(b, a, 'r')
        ax2.set_facecolor('gray')
    if type_graphic_2_var == '2':
        plt.scatter(a, b)
    plt.tight_layout()
    plt.show()
