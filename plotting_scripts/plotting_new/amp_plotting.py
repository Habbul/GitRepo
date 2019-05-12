from plotting_new import *

names = ['VOLTAGE_0.15-0.2V', 'VOLTAGE_0.15-0.30000000000000004V', 'VOLTAGE_0.15-0.4V', 'VOLTAGE_0.15-0.5V',
'VOLTAGE_0.15-0.6000000000000001V', 'VOLTAGE_0.15-0.7V', 'VOLTAGE_0.15-0.8V']
input_up_lines_files = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

def averlines_plotting():
	for i in range(1,7):
		s = names[i]
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

						
		xticks =[[i for i in range(0, len(amp_plot))], [str(round(i/60, 1)) for i in data[0][1]]]
		plt.xticks(xticks[0][::20], xticks[1][::20])

		# yticks = yticker(amp_plot, 0.1)
		# plt.yticks(yticks[0], yticks[1])
		
		plt.plot([i/8500 for i in amp_plot])
	# plt.ylim(0, 30000)
	plt.show()

averlines_plotting()