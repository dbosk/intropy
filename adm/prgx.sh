#!/bin/bash

courses="(prgi[2-9][0-9]|prgm2[1-9]|prgm[3-9][0-9])"
components="(LAB[13]|MAT1|KAL1)"

canvaslms results -c "$courses" -A "$components" \
| sed -E "s/ ?[HV]T[0-9]{2}( \(.*\))?//" \
| ladok report -fv

oldIFS="$IFS"
IFS=$'\n'
for course in $(canvaslms courses ${courses} | cut -f 2)
do
	bash ./datorprov.sh "${course}" rapportera
done
IFS="${oldIFS}"

datorprov_courses="(prg[mi]2[2-9]|prg[mi][3-9][0-9])"

canvaslms results -c "$datorprov_courses" -A "LAB2" \
  -S canvaslms.grades.maxgradesurvey \
| sed -E "s/ ?[HV]T[0-9]{2}( \(.*\))?//" \
| ladok report -fv
