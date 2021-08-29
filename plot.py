import justpy as jp
import matplotlib.pyplot as plt

def plot_test():
    wp = jp.WebPage()
    plt.plot([0, 1, 4, 9], marker='*', markersize=20, markeredgecolor='red')
    plt.title('Matplotlib Example')
    plt.xlabel('x data')
    plt.ylabel('y data')
    jp.Matplotlib(a=wp)

    # If memory may be an issue, don't forget to close figures not in use anymore
    plt.close()
    return wp

jp.justpy(plot_test)