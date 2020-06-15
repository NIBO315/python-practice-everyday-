import uuid

for i in range(200):
	seq = str(uuid.uuid1())
	string = ''.join(seq.split('-'))
	with open('ACode.txt', 'a') as fp:
		fp.write(string+'\n')