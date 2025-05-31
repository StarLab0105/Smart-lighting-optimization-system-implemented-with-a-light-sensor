lux_data_day = []
for i in range(11):
    value = int(input("럭스 값 :"))
    lux_data_day.append(value)

# 오후 7 ~ 오전 6시 | 11시간 작동
set_light = 0
max_lux = 2000
min_lux = 100
# 평균 럭스 -> 1000
for i in lux_data_day:
    if lux_data_day[i] > 2000:
        set_light = 0
        lux_data_day[i] = 0
    elif lux_data_day[i] > 1600:
        set_light = 40
        lux_data_day[i] *= 0.6
    elif lux_data_day[i] > 1200:
        set_light = 80
        lux_data_day[i] *= 0.8
    else:
        set_light = 100
        lux_data_day[i] *= 1


______________________________________________________________________________________________________________________________________________________

import numpy as np

lux_01 = np.random.randint(0, 20)
lux_02 = np.random.randint(0, 10)
lux_03 = np.random.randint(0, 15)
lux_04 = np.random.randint(0, 5)
lux_05 = np.random.randint(5, 20)
lux_06 = np.random.randint(20, 100)
lux_07 = np.random.randint(100, 300)
lux_08 = np.random.randint(300, 800)
lux_09 = np.random.randint(800, 1500)
lux_10 = np.random.randint(1500, 2500)
lux_11 = np.random.randint(2500, 4000)
lux_12 = np.random.randint(4000, 6000)
lux_13 = np.random.randint(3500, 5500)
lux_14 = np.random.randint(2500, 4500)
lux_15 = np.random.randint(2000, 3500)
lux_16 = np.random.randint(1000, 2000)
lux_17 = np.random.randint(300, 1000)
lux_18 = np.random.randint(100, 300)
lux_19 = np.random.randint(0, 10)
lux_20 = 0
lux_21 = 0
lux_22 = 0
lux_23 = 0
lux_24 = 0 '

lux_day = [lux_01,lux_02,lux_03,lux_04,lux_05,lux_06,lux_07,lux_08,lux_09,lux_10,lux_11,lux_12,lux_13,lux_14,lux_15,lux_16 ,lux_17,lux_18,lux_19,lux_20,lux_21,lux_22,lux_23,lux_24]




















