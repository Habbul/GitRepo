from plotting_new import *

# names = ['VOLTAGE_0.15-0.2V', 'VOLTAGE_0.15-0.30000000000000004V', 'VOLTAGE_0.15-0.4V', 'VOLTAGE_0.15-0.5V',
# 'VOLTAGE_0.15-0.6000000000000001V', 'VOLTAGE_0.15-0.7V', 'VOLTAGE_0.15-0.8V']
# input_voltages = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

def averlines_plotting():
	names = ['freq_0.02kHz', 'freq_0.12000000000000001kHz', 'freq_0.22000000000000003kHz', 'freq_0.32000000000000006kHz', 
	 'freq_0.42000000000000004kHz', 'freq_0.52kHz']
	# input_voltages = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
	# names = ['DCYCLE_20%', 'DCYCLE_40%', 'DCYCLE_60%', 'DCYCLE_80%',]
	# names = ['VOLTAGE_0.3V', 'VOLTAGE_0.4V', 'VOLTAGE_0.5V', 'VOLTAGE_0.6V', 'VOLTAGE_0.7V',
	# 'VOLTAGE_0.7999999999999999V']
	
	dcycles = [20, 40, 60, 80]
	kHzs = [0.02, 0.12, 0.22, 0.32, 0.42, 0.52]
	input_voltages = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

	for i in range(0,6):
		s = names[i]
		input_voltage = input_voltages[i]

		with open ("{}.txt".format(s), "r") as f:
			ret = f.readlines()
		print(s)

		data = [eval(i) for i in ret]

		amp_plot = []

		n=0
		j=-1
		for sing_snap in data[0][0][5:]:
			j+=1
			filtred_snap = geometry_filter(sing_snap, 200)
			
			# ns_up = new_up_liner(filtred_snap, 1000)
			# ns_down = new_down_liner(filtred_snap, 1000)
			light_p=filtred_snap[0]
			for i in filtred_snap:
				if i> light_p:
					light_p = i
			heavy_p = filtred_snap[0]
			for i in filtred_snap:
				if i<filtred_snap[0]:
					heavy_p = i
			ns_up = [light_p]
			ns_down = [heavy_p]

			if (len(ns_down)!=0)&(len(ns_up)!=0):
				amp_plot.append(middle(ns_up)-middle(ns_down))


		filtred_amp_plot = filterr(amp_plot, 1)

		resistance_plot = [1.2/(i/16000/(input_voltage-0.15)-1) for i in filtred_amp_plot]

		# with open("resistance_plot_tof_rectangular.txt", "w") as f:
		# 	f.write(s + "\n")
		# 	f.write("input_voltage" + str(input_voltage))
		# 	f.write("Amplitudes \n")
		# 	f.write(str(filtred_amp_plot) + "\n")
		# 	f.write("resistance \n")
		# 	f.write(str(resistance_plot) + "\n")

		resistance_plot = filterr(resistance_plot, 1)
		xticks =[[i for i in range(0, len(resistance_plot), 13)], [str(round(i/60, 1)) for i in data[0][1][::13]]]
		plt.xticks(xticks[0][::10], xticks[1][::10])

		# yticks = yticker(amp_plot, 0.1)
		# plt.yticks(yticks[0], yticks[1])

		plt.plot(resistance_plot)
	plt.ylim(0, 5)
	plt.legend(tuple(['{}kHz'.format(i) for i in kHzs[0::]]))
	plt.xlabel('Time, min')
	plt.ylabel('Resistance, MΩ')
	plt.show()

averlines_plotting()