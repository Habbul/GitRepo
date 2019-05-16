from plotting_new import *

names = ['VOLTAGE_0.15-0.3V', 'VOLTAGE_0.15-0.4V', 'VOLTAGE_0.15-0.5V', 'VOLTAGE_0.15-0.6V',
'VOLTAGE_0.15-0.7V', 'VOLTAGE_0.15-0.7999999999999999V']
input_voltages = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

def averlines_plotting():
	for i in range(0,5):
		s = names[i]
		input_voltage = input_voltages[i]

		with open ("{}.txt".format(s), "r") as f:
			ret = f.readlines()
		print(s)

		data = [eval(i) for i in ret]

		amp_plot = []

		n=0
		j=-1
		for sing_snap in data[0][0]:
			j+=1
			filtred_snap = filterr(sing_snap, 20)
			
			ns_up = new_up_liner(filtred_snap, 500)
			ns_down = new_down_liner(filtred_snap, 300)
			if (len(ns_down)!=0)&(len(ns_up)!=0):
				amp_plot.append(s_average(ns_up)-s_average(ns_down))


		filtred_amp_plot = filterr(amp_plot, 4)
		resistance_plot = [1.2/(i/8500/(input_voltage-0.15)-1) for i in filtred_amp_plot]

		xticks =[[i for i in range(0, len(filtred_amp_plot))], [str(round(i/60, 1)) for i in data[0][1][::4]]]
		plt.xticks(xticks[0][::15], xticks[1][::15])

		# yticks = yticker(amp_plot, 0.1)
		# plt.yticks(yticks[0], yticks[1])
		
		plt.plot(resistance_plot)
	plt.ylim(0, 5)
	plt.legend(tuple(['Voltage {}'.format(i) for i in input_up_lines_files[1::]]))
	plt.show()

averlines_plotting()