import pygame
import random
import time
import math

pygame.font.init()
startTime = time.time()

screen = pygame.display.set_mode((900, 650))    # Total window size
pygame.display.set_caption("S E A R C H   A L G O R I T H M S   V I S U A L I S E R")   # Window title

run = True

width = 900
length = 600
array = [0] * 151
N = len(array)
key = 0
foundkey = False
lo = 0
hi = len(array) - 1

arr_clr = [(176, 196, 222)] * 151
clr_ind = 0
clr = [(176, 196, 222), (255, 0, 0), (70, 130, 180), (0,255,0)]

bigfont = pygame.font.SysFont("Verdana", 70)
fnt = pygame.font.SysFont("Verdana", 30)
fnt1 = pygame.font.SysFont("Verdana", 16)


def heapSort(array):

    for i in range(N // 2 - 1, -1, -1):
        heapify(array, i, N)
    for i in range(N - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, 0, i)


def heapify(array, root, size):
    left = root * 2 + 1
    right = root * 2 + 2
    largest = root

    if left < size and array[left] > array[largest]:
        largest = left
    if right < size and array[right] > array[largest]:
        largest = right
    if largest != root:
        array[largest], array[root] = array[root], array[largest]
        heapify(array, largest, size)


def generate_arr(): # Function to generate new Array
    for i in range(1, 151):
        arr_clr[i] = clr[0]
        array[i] = random.randrange(1, 100)
    heapSort(array)
generate_arr()


def refill():   # Function to refill the updates on the window
    screen.fill((255, 255, 255))
    draw()
    pygame.display.update()
    pygame.time.delay(500)


def linear_search(array, key):    # O(n)
    for index, value in enumerate(array):
        arr_clr[index] = clr[1]
        refill()
        arr_clr[index] = clr[0]
        refill()
        if value == key:
            arr_clr[index] = clr[3]
            refill()
            return 1
    return -1


def binary_search(array, key):      # O(Log n)
    lo = 0
    hi = len(array) - 1

    while lo < hi:
        mid = lo + (hi - lo) // 2
        if array[mid] == key:
            arr_clr[mid] = clr[3]
            refill()
            return 1
        elif array[mid] < key:
            arr_clr[mid] = clr[1]
            refill()
            arr_clr[mid] = clr[0]
            refill()
            lo = mid + 1
        else:
            arr_clr[mid] = clr[2]
            refill()
            arr_clr[mid] = clr[0]
            refill()
            hi = mid - 1
        refill()
    return -1


def binary_search_recursive(array, lo, hi, key):
    if hi >= lo:
        mid = lo + (hi - lo) // 2
        if array[mid] == key:
            arr_clr[mid] = clr[0]
            refill()
            arr_clr[mid] = clr[3]
            refill()
            return 1
        elif array[mid] > key:
            arr_clr[mid] = clr[2]
            refill()
            arr_clr[mid] = clr[0]
            refill()
            return binary_search_recursive(array, lo, mid - 1, key)
        else:
            arr_clr[mid] = clr[1]
            refill()
            arr_clr[mid] = clr[0]
            refill()
            return binary_search_recursive(array, mid + 1, hi, key)
    else:
        return -1


def jump_search(array, key, N):    # O(vn)
    step = math.sqrt(N)
    prev = 0
    while array[int(min(step, N) - 1)] < key:
        arr_clr[int(prev)] = clr[1]
        refill()
        arr_clr[int(prev)] = clr[0]
        refill()
        prev = step
        step += math.sqrt(N)
        if prev >= N:
            return -1
    while array[int(prev)] < key:
        arr_clr[int(prev)] = clr[1]
        refill()
        arr_clr[int(prev)] = clr[0]
        refill()
        prev += 1
        if prev == min(step, N):
            return -1
    if array[int(prev)] == key:
        arr_clr[int(prev)] = clr[0]
        refill()
        arr_clr[int(prev)] = clr[3]
        refill()
        return 1
    refill()
    return -1


def interpolation_search(array, lo, hi, key):       # O(log log n)
    if (lo <= hi and key >= array[lo] and key <= array[hi]):
        pos = lo + ((hi - lo) // (array[hi] - array[lo]) * (key - array[lo]))
        if array[pos] == key:
            arr_clr[pos] = clr[0]
            refill()
            arr_clr[pos] = clr[3]
            refill()
            return 1
        if array[pos] < key:
            arr_clr[pos] = clr[1]
            refill()
            arr_clr[pos] = clr[0]
            refill()
            return interpolation_search(array, pos + 1, hi, key)
        if array[pos] > key:
            arr_clr[pos] = clr[2]
            refill()
            arr_clr[pos] = clr[0]
            refill()
            return interpolation_search(array, lo, pos - 1, key)
    return -1


def exponential_search(array, N, key):    # O(Log n)
    if array[0] == key:
        return 1
    i = 1
    while i < N and array[i] <= key:
        arr_clr[i] = clr[1]
        refill()
        arr_clr[i] = clr[0]
        refill()
        i = i * 2
    return binary_search_recursive(array, int(i / 2), min(i, N - 1), key)


def fibonacci_search(array, key):
    start = -1
    f0 = 0
    f1 = 1
    f2 = 1
    while (f2 < N):
        f0 = f1
        f1 = f2
        f2 = f1 + f0
    while (f2 > 1):
        index = min(start + f0, N - 1)
        if array[index] < key:
            arr_clr[index] = clr[1]
            refill()
            arr_clr[index] = clr[0]
            refill()
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index
        elif array[index] > key:
            arr_clr[index] = clr[2]
            refill()
            arr_clr[index] = clr[0]
            refill()
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            arr_clr[index] = clr[0]
            refill()
            arr_clr[index] = clr[3]
            refill()
            return 1
    if (f1) and (array[N - 1] == key):
        return length - 1
    return -1


def draw():     # Function to Draw the array values

    txt0 = fnt1.render("To RESET number, press [R]", 1, (0, 0, 0))  # The text that is rendered
    screen.blit(txt0, (20, 10))                                     # Position of the text
    txt1 = fnt1.render("For a NEW array, press [N]", 1, (0, 0, 0))
    screen.blit(txt1, (20, 30))
    txt2 = fnt1.render("To search, press: [L]inear, [B]inary, [J]ump", 1, (0, 0, 0))
    screen.blit(txt2, (20, 50))
    txt3 = fnt1.render("[I]nterpolation,  [E]xponential,  [F]ibonacci", 1, (0, 0, 0))
    screen.blit(txt3, (20, 70))

    text0 = fnt1.render("Enter a number to search for: " + str(key), 1, (0, 0, 0))
    screen.blit(text0, (600, 20))
    text1 = fnt1.render("Elapsed Time: " + str(int(time.time() - startTime)), 1, (0, 0, 0))
    screen.blit(text1, (730, 50))

    element_width = (width - 150) // 150
    boundry_arr = 900 / 150
    boundry_grp = 550 / 100
    pygame.draw.line(screen, (0, 0, 0), (0, 95), (900, 95), 6)


    for i in range(1, 151):    # Drawing the array values as lines
        pygame.draw.line(screen, arr_clr[i], (boundry_arr * i-3, 650), (boundry_arr * i-3, 650 - (array[i] * boundry_grp)), element_width)
    if foundkey == 1:
        text = bigfont.render("Number Found", 1, (0, 0, 0))
        screen.blit(text, (200, 300))
    elif foundkey == -1:
        text = bigfont.render("Number Not Found", 1, (0, 0, 0))
        screen.blit(text, (100, 300))


while run:  # Program should be run continuously to keep the window open

    screen.fill((255, 255, 255))

    for event in pygame.event.get():    # Event handler stores all event

        if event.type == pygame.QUIT:        # If we click Close button in window
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                key = 0
                foundkey = 0
                generate_arr()
            if event.key == pygame.K_r:
                foundkey = 0
                key = 0
                for i in range(0, len(array)):
                    arr_clr[i] = clr[0]
            if event.key == pygame.K_l and key != 0:
                foundkey = linear_search(array, key)
            if event.key == pygame.K_b and key != 0:
                foundkey = binary_search(array, key)
            if event.key == pygame.K_j and key != 0:
                foundkey = jump_search(array, key, N)
            if event.key == pygame.K_i and key != 0:
                foundkey = interpolation_search(array, lo, hi, key)
            if event.key == pygame.K_e and key != 0:
                foundkey = exponential_search(array, N, key)
            if event.key == pygame.K_f and key != 0:
                foundkey = fibonacci_search(array, key)
            if event.key == pygame.K_0:
                key = key * 10
            if event.key == pygame.K_1:
                key = key * 10 + 1
            if event.key == pygame.K_2:
                key = key * 10 + 2
            if event.key == pygame.K_3:
                key = key * 10 + 3
            if event.key == pygame.K_4:
                key = key * 10 + 4
            if event.key == pygame.K_5:
                key = key * 10 + 5
            if event.key == pygame.K_6:
                key = key * 10 + 6
            if event.key == pygame.K_7:
                key = key * 10 + 7
            if event.key == pygame.K_8:
                key = key * 10 + 8
            if event.key == pygame.K_9:
                key = key * 10 + 9
    draw()
    pygame.display.update()

pygame.quit()