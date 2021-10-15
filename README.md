# pomo
Simplifications for python works with data (xls to dict, dict to xls, easy threading)


## Write files easier

### It wrires data from test to test.json

test = [0,"hello", {"a": "world", "b": "!"}]

write_j(test)

### If you need to put you own name for the file or write file to the path, just add arg file_name = 'your path'

write_j(test, file_name='dist/my_file.txt')




