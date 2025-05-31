import numpy as np
import matplotlib.pyplot as plt


lux_02 = np.random.randint(0, 10)
lux_04 = np.random.randint(0, 5)
lux_05 = np.random.randint(5, 20)
lux_06 = np.random.randint(20, 100)
lux_07 = np.random.randint(100, 300)
lux_08 = np.random.randint(300, 800)
lux_09 = np.random.randint(800, 1500)
lux_10 = np.random.randint(1500, 2500)
lux_11= np.random.randint(2500, 4000)
lux_12= np.random.randint(4000, 6000)
lux_13= np.random.randint(3500, 5500)
lux_14= np.random.randint(2500, 4500)
lux_15= np.random.randint(2000, 3500)
lux_16= np.random.randint(1000, 2000)
lux_17= np.random.randint(300, 1000)
lux_18= np.random.randint(100, 300)
lux_19= np.random.randint(0, 10)

lux_day = [lux_02,lux_04,lux_05,lux_06,lux_07,lux_08,lux_09,lux_10,lux_11,lux_12,lux_13,lux_14,lux_15,lux_16
            ,lux_17,lux_18,lux_19]
print(lux_day)


plt.title("Smart-lighting-optimization-system-implemented-with-a-light-sensor")
plt.ylabel("lux")
plt.xlabel("time")
plt.ylim(0,6000)
plt.xlim(0,24)
plt.plot(lux_day)
plt.show()
