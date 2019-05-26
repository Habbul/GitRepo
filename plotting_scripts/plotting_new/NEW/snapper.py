from plotting_new import *

def snapper():
	names = ['VOLTAGE_0.15-0.2V', 'VOLTAGE_0.15-0.30000000000000004V', 'VOLTAGE_0.15-0.4V', 'VOLTAGE_0.15-0.5V',
'VOLTAGE_0.15-0.6000000000000001V', 'VOLTAGE_0.15-0.7V', 'VOLTAGE_0.15-0.8V']
	input_voltages = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
	
	for i in range(1,7):
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
			plt.ylim(0,15000)
			plt.plot(sing_snap, color = 'b')
			ns_up = new_up_liner(filtred_snap, 100)
			ns_down = new_down_liner(filtred_snap, 100)
			# plt.plot(filtred_snap, color='b')
			plt.savefig('snaps/snap{}.png'.format(j+1))
			plt.clf()
			plt.subplot(1,2,1)
			plt.ylim(0, 10000)
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
			plt.ylim(0, 10000)
			plt.plot(sing_snap)
			# for t in ns_up:
			# 	plt.plot([t for l in sing_snap])
			# for t in ns_down:
			# 	plt.plot([t for l in sing_snap])
			if len(ns_up)!=0:
				plt.plot([middle(ns_up) for i in sing_snap])
			if len(ns_down)!=0:
				plt.plot([middle(ns_down) for i in sing_snap])
			plt.show()
			plt.clf()
			print('snap{}'.format(j+1))
			########################################################

snapper()