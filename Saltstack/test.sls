#!py
def run():
	example={}
	example['/tmp/test'] = {
		'file.managed':[
		{'source':'salt://test'},
		{'mode':'644'},
		{'user':'root'},
		{'template':'nginx'},
		{'group':'root'},
		{'context':{
		'a':__grains__['os'],
		'b':__pillar__['a'],
		},
		},
		],
		}
	return example
