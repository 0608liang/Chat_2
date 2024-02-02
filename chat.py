#盡量使用變數去簡化自己的程式碼

#讀取功能
def read_file(filename) :
	lines = []
	with open(filename, 'r', encoding = 'utf-8') as f :
		for line in f :
			lines.append(line.strip())

	return lines

#轉換功能
def convert(lines) :
	person = None
	new = []
	for line in lines :
		if line == 'Allen' :
			person = 'Allen'
			continue
		elif line == 'Tom' :
			person = 'Tom'
			continue

		#如果person有值才執行這行
		if person :
			new.append(person + ': ' + line)
	return(new)

def write_file(filename, lines) :
	with open(filename, 'w') as f :
		for line in lines :
			f.write(line + '\n')

#主程式
def main() :
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

#程式進入點
main() 
