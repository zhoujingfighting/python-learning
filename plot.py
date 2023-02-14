import matplotlib.pyplot as plt

x = [2,4,6,8]

y = [2,4,6,8]

tick_label = ["one", "two", "three", "four"]

plt.bar(x,y,tick_label=tick_label,width=0.8, color=["blue","cyan"])

plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.title("Demo Graph - Bar Chart")
plt.show()