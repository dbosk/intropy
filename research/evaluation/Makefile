.PHONY: all
all: survey-prgm21.csv survey-prgi21.csv

survey-prgm21.csv: prgm21.csv
	echo "First name,Last name,Organisation,E-mail" > $@
	sed -E "s/^([^,]*),([^,]*),([^,]*),([^,]*)$$/\3,\4,\1,\2/" \
		$^ >> $@

survey-prgi21.csv: prgi21.csv
	echo "First name,Last name,Organisation,E-mail" > $@
	sed -E "s/^([^,]*),([^,]*),([^,]*),([^,]*)$$/\3,\4,\1,\2/" \
		$^ >> $@

prgm21.csv:
	canvaslms -d, users -sc "DD1310HT213" -S | sed "s/\r//" > $@

prgi21.csv:
	canvaslms -d, users -sc "DD1315HT21" -S | sed "s/\r//" > $@

.PHONY: clean
clean:
	${RM} prgm21.csv survey-prgm21.csv
	${RM} prgi21.csv survey-prgi21.csv
