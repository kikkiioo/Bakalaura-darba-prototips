from math import sqrt
import random
from PIL import *


def get_points_from_image(image):
    platums = image.width
    augstums = image.height
    jaunais_izmers = (platums // 3, augstums // 3)
    mainita_izmera_attels = image.resize(jaunais_izmers)
    RGBattels = mainita_izmera_attels.convert("RGB")
    platums = RGBattels.width
    augstums = RGBattels.height
    punkti = []
    for y in range(augstums):
        for x in range(platums):
            krasa = RGBattels.getpixel((x, y))
            punkti.append(krasa)
    return punkti


def eiklida_attalums(punkts1, punkts2):
    summa = 0
    for i in range(len(punkts1)):
        starpiba = punkts1[i] - punkts2[i]
        kvadrats = starpiba * starpiba
        summa += kvadrats
    attalums = sqrt(summa)
    return attalums


def calculate_center(points):
    n_dimensions = len(points[0])

    dimension_sum = []
    for i in range(n_dimensions):
        dimension_sum.append(0.0)

    for point in points:
        for i in range(n_dimensions):
            dimension_sum[i] += point[i]

    coordinates = []
    for v in dimension_sum:
        coordinates.append(v / len(points))

    return coordinates


def assign_points_to_clusters(clusters, points):
    clusters_points = []
    for i in range(len(clusters)):
        clusters_points.append([])

    for point in points:
        smallest_distance = float("inf")
        index = 0
        for i in range(len(clusters)):
            distance = eiklida_attalums(point, clusters[i]["center"])
            if distance < smallest_distance:
                smallest_distance = distance
                index = i
        clusters_points[index].append(point)

    return clusters_points


def fit_points_to_clusters(punkti, n_clusters, min_diff):
    klasteri = []
    nejausi_punkti = random.sample(punkti, n_clusters)
    for point in nejausi_punkti:
        klasteris = {"center": point, "points": [point]}
        klasteri.append(klasteris)

    while True:
        clusters_points = assign_points_to_clusters(klasteri, punkti)
        max_diff = 0
        for i in range(len(klasteri)):
            if not clusters_points[i]:
                continue
            old_center = klasteri[i]["center"]
            new_center = calculate_center(clusters_points[i])
            klasteri[i]["center"] = new_center
            max_diff = max(max_diff, eiklida_attalums(old_center, new_center))
        if max_diff < min_diff:
            break

    return klasteri


def get_colors_from_image(image_filename, n_colors):
    punkti = get_points_from_image(image_filename)
    clusters = fit_points_to_clusters(punkti, n_colors, min_diff=2)
    clusters.sort(key=lambda c: len(c["points"]), reverse=True)
    rgb_values = []
    for c in clusters:
        center = c["center"]
        center_int = [int(val) for val in center]
        center_tuple = tuple(center_int)
        rgb_values.append(center_tuple)
    return rgb_values
