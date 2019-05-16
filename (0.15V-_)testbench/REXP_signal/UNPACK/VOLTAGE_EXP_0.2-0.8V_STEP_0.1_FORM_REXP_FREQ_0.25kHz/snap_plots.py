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


for i in range(1,7):
	s = names[i]
	with open ("{}.txt".format(s), "r") as f:
		ret = f.readlines()
	print(s)


	data = [eval(i) for i in ret]
	n=0

	amp_plot = []

	for i in range(1, len(data[0][0])):
		sing_snap = data[0][0][i]
		filtred_snap = filter(sing_snap, 10)

		light_p = filtred_snap[0]
		heavy_p = filtred_snap[0]
		d_lines = []

		for j in filtred_snap:
			if light_p<j:
				light_p = j
			if heavy_p>j:
				heavy_p = j
			if ((j-heavy_p>500) & (light_p-heavy_p>500) & (light_p != j)):
				# plt.plot([heavy_p for l in filtred_snap], color='g')
				d_lines.append(heavy_p)
				heavy_p = j
				light_p = j

		light_p = filtred_snap[0]
		heavy_p = filtred_snap[0]
		up_lines = []

		for j in filtred_snap:
			if light_p<j:
				light_p = j
			if heavy_p>j:
				heavy_p = j
			if ((j-light_p<-700) & (light_p-heavy_p>700) & (light_p != j)):
				up_lines.append(light_p)
				# plt.plot([light_p for l in filtred_snap], color='r')
				heavy_p = j
				light_p = j

		# plt.plot([s_average(d_lines) for l  in filtred_snap], color='r')
		# plt.plot([s_average(up_lines) for l in filtred_snap], color='g')

		amp_plot.append(s_average(up_lines)-s_average(d_lines))

		# plt.plot(filter(sing_snap, 10), color='b')
		# plt.savefig('snaps/snap{}'.format(i+1))
		# plt.clf()
		print('snap{}'.format(i+1))

	plt.plot(filter(amp_plot, 5))


plt.savefig('snaps/general_amp_plot.png')
print('amp_plot builded')


# with open("pictures/{}.png".format(names[i]), 'w'):