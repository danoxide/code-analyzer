#-*-coding: utf-8-*-
#!/usr/bin/python
import sys, os, os.path

# typy plików do sprawdzenie
exts = ('cpp', 'h', 'py')

lines = 0
files = 0
for root, dirnames, filenames in os.walk(os.path.dirname(os.path.abspath(__file__))):
	for filename in filenames:
		if filename.endswith(exts) and filename != sys.argv[0]:
			lines += len(open('/'.join([root, filename])).readlines());
			files += 1

print "Linii kodu:", lines
print "Łącznie plików:", files
