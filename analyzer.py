#-*-coding: utf-8-*-
#!/usr/bin/python
import sys, os, os.path, zipfile, shutil;
import pprint, mmap, time;
from subprocess import call;

# Pobera rozszerzenie pliku
def get_extension(file_name):
	return file_name.split('.')[-1];

# Domyślne ustawienia aplikacji
defaults = {
	'file' : sys.argv[1], # zmienić póxniej na sys.argv[0]
	'tmp' : 'tmp/',
	'types' : ('php', 'html', 'js', 'css', 'cpp', 'h', 'py') # lista dostępnych rozszerzeń
};

f = defaults['file']; # nazwa pliku
t = defaults['tmp']; # nazwa katalogu tymczasowego
l = 0; # liczba lini kodu

if get_extension(f) == 'zip':
	# Stworzenie katalogu tymczasowego jeśli go nie ma
	print "Tworzenie katalogu tymczasowego tmp/";
	if not os.path.exists(t):
		os.mkdir(t);

	# Otwieranie
	print "Otwranie", f;
	myzip = zipfile.ZipFile(f, 'r');

	allfiles = myzip.namelist();
	# Sprawdzenie wszystkich plików w archiwum
	for member in allfiles:
		filename = os.path.basename(member);
		# pomicięcie jeśli to jest katalog
		if not filename or get_extension(filename) not in defaults['types']:
			continue;

		newname = os.path.join(t, filename);
		source = myzip.open(member);
		target = file(newname, "wb");

		print "Kopiowanie", newname, get_extension(filename);
		with source, target:
			shutil.copyfileobj(source, target);
		
		# Liczenie lini kodu
		with open(newname) as foo:
			l += len(foo.readlines());

	# Zamknięcie uchwytu
	myzip.close();

	print "Czyszczenie...";
	call(['rm', '-rf', t]);

	print "\nLini kodu: ", l;
else:
	print "Zły format pliku...\n";
