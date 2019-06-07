from plotting_new import *

def snapper():
	# names = ['FREQ_0.02kHz', 'FREQ_0.22000000000000003kHz', 'FREQ_0.32000000000000006kHz', 
	# 'VOLTAGE_0.15-0.6V', 'FREQ_0.42000000000000004kHz', 'FREQ_0.52kHz']
	names = ['DCYCLE_20%', 'DCYCLE_40%', 'DCYCLE_60%', 'DCYCLE_80%',]
	# input_voltages = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

	dcycle =  [20, 40, 60, 80]
	for i in range(0,4):
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
			filtred_snap_upper = filterr(sing_snap, 10)	
			filtred_snap_lower = filterr(sing_snap, 10)
			filtred_snap = geometry_filter(sing_snap, 200)
			######SNAP#############################################
			# new_down_liner(filtred_snap, 300)
			# plt.ylim(-15000,15000)
			plt.plot(sing_snap, color = 'b')
			ns_up = new_up_liner(filtred_snap, 1000)
			ns_down = new_down_liner(filtred_snap, 1000)
			# plt.plot(filtred_snap, color='b')
			plt.clf()
			plt.subplot(1,2,1)
			plt.ylim(-30000, 30000)
			plt.plot(filtred_snap)
			# for t in ns_up:
			# 	plt.plot([t for l in filtred_snap])
			# for t in ns_down:
			# 	plt.plot([t for l in filtred_snap])			
			if len(ns_up)!=0:
				plt.plot([middle(ns_up) for i in sing_snap], color = 'r')
			if len(ns_down)!=0:
				plt.plot([middle(ns_down) for i in sing_snap], color = 'r')
			plt.subplot(1,2,2)
			plt.ylim(-30000, 30000)
			plt.plot(sing_snap)
			# for t in ns_up:
			# 	plt.plot([t for l in sing_snap])
			# for t in ns_down:
			# 	plt.plot([t for l in sing_snap])
			if len(ns_up)!=0:
				plt.plot([middle(ns_up) for i in sing_snap])
			if len(ns_down)!=0:
				plt.plot([middle(ns_down) for i in sing_snap])
			# plt.show()
			plt.savefig('snaps/snap{}.png'.format(j+1))			
			plt.clf()
			print('snap{}'.format(j+1))
			########################################################

snapper()