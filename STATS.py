import math

NAME = "unknown"
HP = 100
MAX_HP = 100
XP = 0
XP_ET_LVL = 16.6
XP_SL_LVL = 25
XP_MNOZ = 1.25
LVL = 1
STAMINA = 100
MAX_STAMINA = 100
ststs = dict({1: NAME,
              2: HP,
              3: MAX_HP,
              4: XP,
              5: STAMINA,
              6: MAX_STAMINA,
              7: XP_ET_LVL,
              8: XP_SL_LVL,
              9: LVL})
ststsList = ("Имя - ", "Здоровье = ", "Максимальное здоровье = ", "Опыт = ")


def proschet():
    ststs[8] = math.ceil(ststs[7] * XP_MNOZ)
    if XP >= XP_SL_LVL:
        ststs[9] += 1
        ststs[4] = 0
proschet()