import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
plt.style.use('ggplot')


A = list(range(0, 5))
n = len(A)
random.shuffle(A)


def bogo_sort(A):
    while (is_sorted(A) == False):
        random.shuffle(A)
        yield A


def is_sorted(A):
    for i in range(0, n-1):
        if (A[i] > A[i + 1]):
            return False
    return True


def visualize():

    generator = bogo_sort(A)

    fig, ax = plt.subplots()
    ax.set_title('')
    bar_sub = ax.bar(range(len(A)), A, align="edge")

    ax.set_xlim(0, len(A))
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]

    def update(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text(f"# of operations: {iteration[0]}")

    anim = animation.FuncAnimation(fig, func=update, fargs=(bar_sub, iteration), frames=generator, repeat=True,
                                   blit=False, interval=10, save_count=90000)

    plt.show()
    plt.close()


if __name__ == "__main__":
    visualize()