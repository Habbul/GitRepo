from plotting_new import *

# names = ['VOLTAGE_0.15-0.2V', 'VOLTAGE_0.15-0.30000000000000004V', 'VOLTAGE_0.15-0.4V', 'VOLTAGE_0.15-0.5V',
# 'VOLTAGE_0.15-0.6000000000000001V', 'VOLTAGE_0.15-0.7V', 'VOLTAGE_0.15-0.8V']
# input_up_lines_files = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

def averlines_plotting():
	names = ['FREQ_0.02kHz', 'FREQ_0.12000000000000001kHz', 'FREQ_0.22000000000000003kHz', 'FREQ_0.32000000000000006kHz', 
	 'FREQ_0.42000000000000004kHz', 'FREQ_0.52kHz']
	names = ['DCYCLE_20%', 'DCYCLE_40%', 'DCYCLE_60%', 'DCYCLE_80%', 'DCYCLE_100%']

	# input_voltages = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
	kHzs = [0.02, 0.12, 0.22, 0.32, 0.42, 0.52]
	
	for i in range(4,5):
		s = names[i]
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

			ns_up = new_up_liner(filtred_snap, 1000)
			ns_down = new_down_liner(filtred_snap, 1000)
			if i==4:
				ns_up = [middle(filtred_snap)]
				ns_down = [0.15]
				
			if (len(ns_down)!=0)&(len(ns_up)!=0):
				amp_plot.append(middle(ns_up)-middle(ns_down))

		# yticks = yticker(amp_plot, 0.1)
		# plt.yticks(yticks[0], yticks[1])
		filtred_amp_plot = filterr(amp_plot, 1)		
		plt.plot([i/16000 for i in filtred_amp_plot])
	plt.ylim(-5, 5)
	xticks =[[i for i in range(0, len(filtred_snap), 13)], [str(round(i/60, 1)) for i in data[0][1][::13]]]
	plt.xticks(xticks[0][::10], xticks[1][::10])
	plt.legend(tuple(['{}kHz'.format(i) for i in kHzs[0::]]))
	plt.show()

averlines_plotting()