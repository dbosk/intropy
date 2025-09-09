#!/bin/bash

# Report everything except LAB2

courses="(prgi[2-9][0-9]|prgm2[1-9]|prgm[3-9][0-9])"
components="(LAB[13]|MAT1|KAL1)"

canvaslms results -c "$courses" -A "$components" \
| sed -E "s/ ?[HV]T[0-9]{2}( \(.*\))?//" \
| ladok report -fv

# Report LAB2

NEW_DATORPROV_COURSES="(prgm(2[4-9]|[3-9][0-9])|DD1317 HT(2[5-9]|[3-9][0-9]))"
current=$(date +%Y-%m)
NEW_DATORPROV_EXAMROOMS="DD131[07] LAB2.*${current}"
bash ./datorprov.sh \
  "(${NEW_DATORPROV_COURSES}|${NEW_DATORPROV_EXAMROOMS})" \
  rapportera

datorprov_courses="(prg[mi]2[2-9]|prg[mi][3-9][0-9])"

canvaslms results -c "$datorprov_courses" -A "LAB2" \
  -S canvaslms.grades.maxgradesurvey \
| sed -E "s/ ?[HV]T[0-9]{2}( \(.*\))?//" \
| ladok report -fv
