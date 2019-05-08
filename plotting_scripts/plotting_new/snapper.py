from plotting_new import *

names = ['VOLTAGE_0.15-0.2V', 'VOLTAGE_0.15-0.30000000000000004V', 'VOLTAGE_0.15-0.4V', 'VOLTAGE_0.15-0.5V',
'VOLTAGE_0.15-0.6000000000000001V', 'VOLTAGE_0.15-0.7V', 'VOLTAGE_0.15-0.8V']
input_up_lines_files = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

def snapper():
	names = ['VOLTAGE_0.15-0.2V', 'VOLTAGE_0.15-0.30000000000000004V', 'VOLTAGE_0.15-0.4V', 'VOLTAGE_0.15-0.5V',
'VOLTAGE_0.15-0.6000000000000001V', 'VOLTAGE_0.15-0.7V', 'VOLTAGE_0.15-0.8V']
	input_up_lines_files = [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
	
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

			######SNAP#############################################
			plt.plot([s_average(up_liner(filtred_snap, 20)) for j in filtred_snap])
			plt.plot([s_average(down_liner(filtred_snap, 20)) for j in filtred_snap])
			plt.plot(filtred_snap, color='b')
			plt.savefig('snaps/snap{}.png'.format(j+1))
			plt.clf()
			print('snap{}'.format(j+1))
			########################################################

snapper()