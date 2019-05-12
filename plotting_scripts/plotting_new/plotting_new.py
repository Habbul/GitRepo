import matplotlib.pyplot as plt
import math


names = ['VOLTAGE_0.15-0.2V', 'VOLTAGE_0.15-0.30000000000000004V', 'VOLTAGE_0.15-0.4V', 'VOLTAGE_0.15-0.5V',
'VOLTAGE_0.15-0.6000000000000001V', 'VOLTAGE_0.15-0.7V', 'VOLTAGE_0.15-0.8V']
input_up_lines_files = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]


def s_average(inp):
	acc=0
	for i in inp:
		acc+=i
	return(acc/len(inp))


def filterr(arr, width):
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


def resistance_calc(input_up_lines, output_up_lines):
	#out in Megs
	return[1.2/(i/input_up_lines-1) for i in output_up_lines]


def yticker(inp_data, step):
	#step in volts
	l = 0
	for i in inp_data:
		if l<i: l = i
	yticks_pos = []
	yticks_eval = []
	i=0
	while i<=l/8500:
		yticks_pos.append(round(i*8500))
		i+=step
	i=0
	while i<=l/8500:
		yticks_eval.append(str(round(i, 3)))
		i+=step
	return(yticks_pos, yticks_eval)
	# return([i*8500 for i in range(0, l/8500, step)], [str(i) for i  in range(0, l/8500, step)])

def new_up_liner(snap, hill_height):
	light_p = snap[0]
	heavy_p = snap[0]
	for i in snap:
		if i>light_p:
			light_p=i
		if i<heavy_p:
			heavy_p=i
	level_line = abs((light_p-heavy_p)/2+heavy_p)
	print(level_line)
	

	up_lines=[]
	light_p = level_line
	old_time = 6
	j=-1
	some_lines = []
	overline = False
	if snap[0]> level_line:
		overline = True
	for i in snap:
		if light_p<i:
			light_p=i
		if (i<level_line)&(light_p-level_line>hill_height):
			up_lines.append(light_p)
			light_p=i
	# print(len(up_lines))
	return(up_lines)


def new_down_liner(snap, hill_height):
	light_p = snap[0]
	heavy_p = snap[0]
	for i in snap:
		if i>light_p:
			light_p=i
		if i<heavy_p:
			heavy_p=i
	level_line = abs((light_p-heavy_p)/2+heavy_p)
	print(level_line)
	

	down_lines=[]
	heavy_p = level_line
	old_time = 6
	j=-1
	some_lines = []
	overline = False
	if snap[0]> level_line:
		overline = True
	for i in snap:
		if heavy_p>i:
			heavy_p=i
		if (i>level_line)&(level_line-heavy_p>hill_height):
			down_lines.append(heavy_p)
			heavy_p=i

	# for i in down_lines:
	# 	plt.plot([i for l in snap], color='g')

	# print(len(down_lines))
	return(down_lines)
#################################################################
#####################SNAPPER#####################################
#################################################################
