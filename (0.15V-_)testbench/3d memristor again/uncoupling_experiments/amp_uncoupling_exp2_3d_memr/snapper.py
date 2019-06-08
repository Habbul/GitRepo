from plotting_new import *

def snapper():
	names = ['amp_-0.2', 'amp_-0.1', 'amp_0.0', 'amp_0.1']
	# names = ['DCYCLE_20%', 'DCYCLE_40%', 'DCYCLE_60%', 'DCYCLE_80%',]
	# names = ['freq_0.02', 'freq_0.12000000000000001', 'freq_0.22000000000000003',
	# 'freq_0.32000000000000006', 'freq_0.42000000000000004', 'freq_0.52']

	dcycles =  [20, 40, 60, 80]
	input_voltages = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
	input_voltages_uncoupling = [-0.2, -0.1, 0.0, 0.1]
	kHzs = [0.02, 0.12, 0.22, 0.32, 0.42, 0.52]

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