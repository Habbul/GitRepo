import matplotlib.pyplot as plt

names = ['VOLTAGE_0.15-0.2V', 'VOLTAGE_0.15-0.30000000000000004V', 'VOLTAGE_0.15-0.4V', 'VOLTAGE_0.15-0.5V',
'VOLTAGE_0.15-0.6000000000000001V', 'VOLTAGE_0.15-0.7V', 'VOLTAGE_0.15-0.8V']

def s_average(inp):
	acc=0
	for i in inp:
		acc+=i
	return(acc/len(inp))

def filter(arr, width):
	return([s_average(arr[i:i+width]) for i in range(0, len(arr), width)])

# plt.plot(filter(data[0][0][2], 4))

# n=0
# for i in range(len(data[0][0])-1):
# 	plt.plot(data[0][0][i])
# 	plt.plot(data[0][0][len(data[0][0])-1-i])
# 	plt.savefig("pictures/{}.png".format(n))
# 	plt.clf()
# 	print("pict {}".format(n))
# 	n+=1

def average(inp1, inp2):
    acc = 0
    for i in range(len(inp1)-1):
    	acc+=inp2[i]-inp1[i]
    return(acc/len(inp1))

for i in range(7):
	s = names[i]
	with open ("{}.txt".format(s), "r") as f:
		ret = f.readlines()

	data = [eval(i) for i in ret]

	aver = []
	for i in range(len(data[0][0])-1):
		aver.append(average(filter(data[0][0][1], 4), filter(data[0][0][i+1], 4)))

	# with open("pictures/{}.png".format(names[i]), 'w'):
	plt.plot(aver, label = 's')
	plt.savefig('pictures/{}.png'.format(s))

plt.plot(aver)

plt.show()