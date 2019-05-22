from plotting_new import *

def snapper():
	names = ["VOLTAGE_0.15--0.2V", "VOLTAGE_0.15--0.15000000000000002V", "VOLTAGE_0.15--0.10000000000000002V", "VOLTAGE_0.15--0.05000000000000002V",
 "VOLTAGE_0.15-0", "VOLTAGE_0.15-0.04999999999999999V", "VOLTAGE_0.15-0.09999999999999999V"]
	input_up_lines_files = [-0.2, -0.15, -0.1, -0.05, 0, 0.05, 0.1]
	
	for i in range(6,7):
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

			######SNAP#############################################
			# new_down_liner(filtred_snap, 300)
			# plt.ylim(0,15000)
			ns_up = new_up_liner(filtred_snap, 20)
			ns_down = new_down_liner(filtred_snap, 20)
			if len(ns_up)!=0:
				plt.plot([s_average(ns_up) for i in filtred_snap])
			if len(ns_down)!=0:
				plt.plot([s_average(ns_down) for i in filtred_snap])
			upper_lines = simple_amplituder(filtred_snap, 0.05, 50)[0]
			lower_lines = simple_amplituder(filtred_snap, 0.05, 50)[1]
			plt.plot(upper_lines)
			plt.plot(lower_lines)
			plt.plot(filtred_snap, color='b')
			plt.savefig('snaps/snap{}.png'.format(j+1))
			plt.clf()
			print('snap{}'.format(j+1))
			########################################################

snapper()