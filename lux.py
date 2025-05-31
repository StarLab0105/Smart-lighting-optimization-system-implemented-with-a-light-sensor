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
        lux_data_day[i] = 100
