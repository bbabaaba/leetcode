import re

def input():
	filename = 'input.txt'
	try:
		fp = open(filename,'r')
	except:
		print 'fail to open input.txt . check it whether exists.'
		return False

	try:
		f = fp.read()
	except:
		print 'fail to read input.txt .'
		return False
	finally:
		fp.close()

	if f == '':
		print 'There is no content in input.txt .'
		return False

	final_f = f.splitlines()
	content = []
	[content.append(line.rstrip('\n').strip(' ')) for line in final_f]

	pattern = re.compile(r'^[+-]\d+')
	match = pattern.match(content[0])
	if match:
		return match.group()
	else:
		return False
	
	return 'result'

if __name__=='__main__':
	if input():
		print input()
	else:
		print 'Your testcase should be modified.'