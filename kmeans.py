from math import sqrt
import random
from PIL import *


def iegut_punktus(image):
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


def aprekinat_centru(punkti):
    dimensijas = len(punkti[0])

    dimensiju_summa = []
    for i in range(dimensijas):
        dimensiju_summa.append(0.0)

    for punkts in punkti:
        for i in range(dimensijas):
            dimensiju_summa[i] += punkts[i]

    koordinatas = []
    for j in dimensiju_summa:
        koordinatas.append(j / len(punkti))

    return koordinatas


def pieksirt_punktus_klasteriem(klasteri, punkti):
    klasteru_punkti = []
    for i in range(len(klasteri)):
        klasteru_punkti.append([])

    for punkts in punkti:
        min_distance = float("inf")
        index = 0
        for i in range(len(klasteri)):
            distance = eiklida_attalums(punkts, klasteri[i]["centrs"])
            if distance < min_distance:
                min_distance = distance
                index = i
        klasteru_punkti[index].append(punkts)

    return klasteru_punkti


def ievietot_punktus(punkti, n_klasteri, min_diff):
    klasteri = []
    nejausi_punkti = random.sample(punkti, n_klasteri)
    for punkts in nejausi_punkti:
        klasteris = {"centrs": punkts, "punkti": [punkts]}
        klasteri.append(klasteris)

    while True:
        klasteru_punkti = pieksirt_punktus_klasteriem(klasteri, punkti)
        max_diff = 0
        for i in range(len(klasteri)):
            if not klasteru_punkti[i]:
                continue
            vecais_centrs = klasteri[i]["centrs"]
            jaunais_centrs = aprekinat_centru(klasteru_punkti[i])
            klasteri[i]["centrs"] = jaunais_centrs
            max_diff = max(max_diff, eiklida_attalums(vecais_centrs, jaunais_centrs))
        if max_diff < min_diff:
            break

    return klasteri


def iegut_krasas_no_attela(attela_faila_nosaukums, n_krasas):
    punkti = iegut_punktus(attela_faila_nosaukums)
    klasteri = ievietot_punktus(punkti, n_krasas, min_diff=2)
    klasteri.sort(key=lambda c: len(c["punkti"]), reverse=True)
    rgb_vertibas = []
    for c in klasteri:
        centrs = c["centrs"]
        centrs_int = [int(val) for val in centrs]
        centrs_masivs = tuple(centrs_int)
        rgb_vertibas.append(centrs_masivs)
    return rgb_vertibas
