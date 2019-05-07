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
			filtred_snap = filter(sing_snap, 20)

			#######SNAP#############################################
			# plt.plot([s_average(up_liner(filtred_snap, 30)) for j in filtred_snap])
			# plt.plot([s_average(down_liner(filtred_snap, 30)) for j in filtred_snap])
			# plt.plot(filtred_snap, color='b')
			# plt.savefig('snaps/snap{}.png'.format(j+1))
			# plt.clf()
			# print('snap{}'.format(j+1))
			########################################################

			amp_plot.append(s_average(up_liner(filtred_snap, 30))-s_average(down_liner(filtred_snap, 30)))

		plt.plot(amp_plot)
	plt.show()