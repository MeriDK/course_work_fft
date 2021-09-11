import cv2
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle


def manhatten(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def find_255(edges):
    coords = []
    for i in range(edges.shape[0]):
        for j in range(edges.shape[1]):
            if edges[i][j] == 255:
                coords.append((i, j))
    return coords


def find_distances(edges):
    coords = find_255(edges)
    distances = []

    for i in range(edges.shape[0]):
        print(i, end=' ')
        distance = []

        for j in range(edges.shape[1]):
            if edges[i][j] == 255:
                distance.append(0)
            else:
                p1 = (i, j)
                min_d = manhatten(p1, coords[0])
                for el in coords:
                    if manhatten(p1, el) < min_d:
                        min_d = manhatten(p1, el)
                distance.append(min_d)
        distances.append(distance)
    return distances


def search(d, pattern):
    pcoords = find_255(pattern)
    res = [float('inf'), 0, 0]
    for i in range(len(d) - pattern.shape[0]):
        for j in range(len(d[i]) - pattern.shape[1]):
            t = 0
            for el in pcoords:
                t += d[i + el[0]][j + el[1]]
            if t < res[0]:
                res = [t, i, j]
    return res


def find_pikachu(path):
    img = cv2.imread('img/pikachu.png', 0)
    edges = cv2.Canny(img, 100, 200)
    img1 = cv2.imread(path, 0)
    edges1 = cv2.Canny(img1, 100, 200)

    d = find_distances(edges1)
    r = search(d, edges)

    img1 = cv2.imread(path)
    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    ax = plt.gca()
    rect = Rectangle((r[2], r[1]), edges.shape[0], edges.shape[1], linewidth=2, edgecolor='g', facecolor='none')
    ax.add_patch(rect)
    plt.show()


find_pikachu('img/img1.jpg')


