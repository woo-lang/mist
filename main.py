from woolang.arguments.arguments import WoolangArgumentParser
import sys as sys


argument_parser = WoolangArgumentParser(sys.argv)

# result, error = run('<stdin>', d)

# if error:
# 	print(error.as_string())
# elif result:
# 	if len(result.elements) == 1:
# 		print(repr(result.elements[0]))
# 	else:
# 		print(repr(result))