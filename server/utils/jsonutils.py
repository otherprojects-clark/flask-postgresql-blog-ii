def get_json_with_props(posts) -> dict:
	h = dict([('data', posts)])

	j = {}
	j['data'] = []
	print(len(h['data']))
	for x in range(len(h['data'])):
		i = {}
		i['id'] = h['data'][x][0]
		i['title'] = h['data'][x][1]
		i['content'] = h['data'][x][2]
		i['createdat'] = h['data'][x][3]
		i['updatedat'] = h['data'][x][4]
		j['data'].append(i)

	return j
