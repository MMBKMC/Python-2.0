import basif

while True:
	text = input('python 2.0 > ')
	if text.strip() == "": continue
	result, error = basif.run('<stdin>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))