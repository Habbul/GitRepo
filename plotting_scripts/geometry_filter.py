def geometry_filter(inp_data):
	return([(inp_data[i-1]+inp_data[i])/2 for i in range(1, len(inp_data), 2)])