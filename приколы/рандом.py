import random
for i in range(1000000):
    a = random.randrange(0, 10000000)
    f = open("%d.txt" %a, "a")
    f.write("1")
    f.close()
