#!/bin/bash

# Report LAB2

#NEW_DATORPROV_COURSES="(prgm(2[4-9]|[3-9][0-9])|DD1317 HT(2[5-9]|[3-9][0-9]))"
NEW_DATORPROV_COURSES="(DD1317 HT(2[5-9]|[3-9][0-9]))"
current=$(date +%Y-%m)
#NEW_DATORPROV_EXAMROOMS="DD131[07] LAB2.*${current}"
NEW_DATORPROV_EXAMROOMS="DD1317.*LAB2.*${current}"
bash ./datorprov.sh \
  "(${NEW_DATORPROV_COURSES}|${NEW_DATORPROV_EXAMROOMS})" \
  rapportera

datorprov_courses="DD1317.*LAB2.*${current}"

canvaslms results -c "$NEW_DATORPROV_COURSES" -A "LAB2" \
| sed -E "s/ ?[HV]T[0-9]{2}( \(.*\))?//" \
| ladok report -fv
