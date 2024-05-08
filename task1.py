
from pprint import pprint
file_name = 'my soul.txt'
file = open(file_name, mode='r')
file_content = file.read()
file.close()
pprint(file_content)