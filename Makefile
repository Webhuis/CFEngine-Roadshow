cf := $(wildcard *.cf) $(wildcard */*.cf) $(wildcard */*/*.cf)
pwd := $(shell pwd)

check:
	$(foreach x,$(cf),cf-promises -c $(x);)

# assumes you have masterfiles.git checked out in the parent directory
masterfiles-sync:
	(cd ../masterfiles; ./autogen.sh --prefix=$(pwd)/policies && make install)
