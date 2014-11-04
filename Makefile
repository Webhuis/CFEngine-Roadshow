cf := $(wildcard *.cf) $(wildcard */*.cf) $(wildcard */*/*.cf)

check:
	$(foreach x,$(cf),cf-promises -c $(x);)

# assumes you have masterfiles.git checked out in the parent directory
libdir:
	rsync -a --delete ../masterfiles/lib/ masterfiles/lib/
