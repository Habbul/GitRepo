from plotting_new import *


def averlines_plotting():
	names = ["VOLTAGE_0.15--0.2V", "VOLTAGE_0.15--0.15000000000000002V", "VOLTAGE_0.15--0.10000000000000002V", "VOLTAGE_0.15--0.05000000000000002V",
 "VOLTAGE_0.15-0", "VOLTAGE_0.15-0.04999999999999999V", "VOLTAGE_0.15-0.09999999999999999V"]
	input_up_lines_files = [-0.2, -0.15, -0.1, -0.05, 0, 0.05, 0.1]
	
	for i in range(0,7):
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
			filtred_snap = filterr(sing_snap, 10)

			ns_up = new_up_liner(filtred_snap, 500)
			ns_down = new_down_liner(filtred_snap, 300)
			if (len(ns_down)!=0)&(len(ns_up)!=0):
				amp_plot.append(s_average(ns_up)-s_average(ns_down))

						


		# yticks = yticker(amp_plot, 0.1)
		# plt.yticks(yticks[0], yticks[1])
		filtred_amp_plot = filterr(amp_plot, 4)
		plt.plot([i/8500 for i in filtred_amp_plot])
	# plt.ylim(0, 30000)
	xticks =[[i for i in range(0, len(filtred_amp_plot))], [str(round(i/60, 1)) for i in data[0][1][::4]]]
	plt.xticks(xticks[0][::15], xticks[1][::15])
	plt.legend(tuple(['Amplitude 0.15-{}V'.format(i) for i in input_up_lines_files[0::]]))
	plt.show()

averlines_plotting()