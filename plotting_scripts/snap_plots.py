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


for i in range(7):
	s = names[i]
	with open ("{}.txt".format(s), "r") as f:
		ret = f.readlines()
	print(s)
	data = [eval(i) for i in ret]
	n=0
	for i in data[0][0]:
		n+=1
		plt.plot(i)
		plt.savefig('snaps/snap{}.png'.format(n))
		plt.clf()
		print('snap {}'.format(n))
	# with open("pictures/{}.png".format(names[i]), 'w'):