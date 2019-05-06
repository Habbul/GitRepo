import matplotlib.pyplot as plt
import math

names = ['VOLTAGE_0.15-0.2V', 'VOLTAGE_0.15-0.30000000000000004V', 'VOLTAGE_0.15-0.4V', 'VOLTAGE_0.15-0.5V',
'VOLTAGE_0.15-0.6000000000000001V', 'VOLTAGE_0.15-0.7V', 'VOLTAGE_0.15-0.8V']

def s_average(inp):
	acc=0
	for i in inp:
		acc+=i
	return(acc/len(inp))


def filter(arr, width):
	return([s_average(arr[i:i+width]) for i in range(0, len(arr), width)])


def geometry_filter(inp_data):
	return([(inp_data[i-1]+inp_data[i])/2 for i in range(1, len(inp_data), 2)])


def up_liner(inp_data, signal_width):
	#width in divs ofc
	light_p = inp_data[math.ceil(signal_width/3)-1]
	heavy_p = inp_data[math.ceil(signal_width/3)-1]
	count = 0
	up_lines = []
	flag = False
	for i in inp_data[math.ceil(signal_width/3)-1:]:
		if i>inp_data[count]:
			flag = True
		if light_p<i:
			light_p = i
		if heavy_p>i:
			heavy_p = i
		if ((i<inp_data[count]) & flag):
			up_lines.append(light_p)
			heavy_p = i
		if inp_data[count]==heavy_p:
			light_p=i

		count+=1
	return(up_lines)


def down_liner(inp_data, signal_width):
	#width in divs ofc
	light_p = inp_data[math.ceil(signal_width/3)-1]
	heavy_p = inp_data[math.ceil(signal_width/3)-1]
	count = 0
	down_lines = []
	flag = False
	for i in inp_data[math.ceil(signal_width/3)-1:]:
		if i<inp_data[count]:
			flag = True
		if light_p<i:
			light_p = i
		if heavy_p>i:
			heavy_p = i
		if ((i>inp_data[count]) & flag):
			down_lines.append(heavy_p)
			light_p = i
		if inp_data[count]==light_p:
			heavy_p=i

		count+=1
	return(down_lines)



for i in range(1,7):
	s = names[i]
	with open ("{}.txt".format(s), "r") as f:
		ret = f.readlines()
	print(s)


	data = [eval(i) for i in ret]
	n=0

	amp_plot = []
	up_line_plot_data = []


	FILTER_HEIGHT = 6000

	for i in range(1, len(data[0][0])):
		sing_snap = data[0][0][i]
		filtred_snap = filter(sing_snap, 20)

		light_p = filtred_snap[0]
		heavy_p = filtred_snap[0]
		d_lines = []

		for j in filtred_snap:
			if light_p<j:
				light_p = j
			if heavy_p>j:
				heavy_p = j
			if ((j-heavy_p>FILTER_HEIGHT) & (light_p-heavy_p>FILTER_HEIGHT) & (light_p != j)):
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
			if ((j-light_p<-FILTER_HEIGHT) & (light_p-heavy_p>FILTER_HEIGHT) & (light_p != j)):
				up_lines.append(light_p)
				# plt.plot([light_p for l in filtred_snap], color='r')
				heavy_p = j
				light_p = j

		

		# plt.ylim(0, 15000)
		# plt.plot([s_average(d_lines) for l  in filtred_snap], color='r')
		# plt.plot([s_average(up_lines) for l in filtred_snap], color='g')

		# amp_plot.append(s_average(up_liner(filtred_snap, 50))-s_average(down_liner(filtred_snap, 50)))
		# up_line_plot_data.append(s_average(up_lines))

		plt.ylim(0, 15000)
		# plt.plot(filtred_snap)
		plt.plot([s_average(up_liner(filtred_snap, 50)) for j in filtred_snap])
		plt.plot([s_average(down_liner(filtred_snap, 50)) for j in filtred_snap])
		plt.plot(filtred_snap, color='b')
		plt.savefig('snaps/snap{}.png'.format(i+1))
		plt.clf()
		print('snap{}'.format(i+1))
	# plt.plot(amp_plot)
	# plt.show()
	# g_count = 0
	# ret = amp_plot
	# for g in range(g_count):
	# 	ret = geometry_filter(ret)
	# plt.plot(ret)

	# plt.plot(up_line_plot_data)

# plt.ylim(0, 50000)
# plt.savefig('snaps/general_amp_plot.png')
plt.show()
# print('amp_plot builded')


# with open("pictures/{}.png".format(names[i]), 'w'):