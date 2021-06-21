import os
import matplotlib.pyplot as plt
import matplotlib.text as text
from board import streets

def displayResults (results):
    fig, ax = plt.subplots()

    labels = []
    for s in streets:
        labels.append(s.name)

    ax.barh(range(40), results)
    ax.set_yticks(range(40))
    ax.set_yticklabels(labels)
    #plt.setp(ax.get_xticklabels(), rotation=90, ha="right", rotation_mode="anchor")
    plt.show()

if __name__ == "__main__":
    os.system("python main.py")