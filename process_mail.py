#Meeting, Assignment, Class

def process_text(message, keyword):
	
	raw = message;

	#Finding Keyword
	Keyword = keyword + ":"
	length = len(keyword)
	index = raw.index(Keyword)
	index = index + length + 2
	count = index
	typeof = ""

	while raw[count]!= "\n":
		count += 1
	
	type_name = raw[index:count]
	return type_name

