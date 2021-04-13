from matplotlib import pyplot as plt
x = [x for x in range(1, 11)]
linear = []
quad = []

for number in range(len(x)):
    linear.append(1.5 * number)
    quad.append(number**2)

plt.figure("lin")
plt.clf()
plt.plot(x, linear, label="lin mate")
plt.legend(loc="upper center")
plt.title("plotting shit")
plt.xlabel("x-axis bro")
plt.ylabel("dats the y-axis")
plt.ylim(0, 15)

plt.figure("quad")
plt.clf()
plt.plot(x, quad, "g-", label="quadratic mate")
plt.legend(loc="upper center")
plt.title("plotting shit")
plt.xlabel("x-axis bro")
plt.ylabel("dats the y-axis")

plt.figure("test")
plt.clf()
plt.plot(x, linear, label="lin")
