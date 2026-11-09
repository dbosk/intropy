#!/bin/bash

# Report LAB2

#NEW_DATORPROV_COURSES="(prgm(2[4-9]|[3-9][0-9])|DD1317 HT(2[5-9]|[3-9][0-9]))"
NEW_DATORPROV_COURSES="(DD1317 HT(2[5-9]|[3-9][0-9]))"
current=$(date +%Y-%m)
#NEW_DATORPROV_EXAMROOMS="DD131[07] LAB2.*${current}"
NEW_DATORPROV_EXAMROOMS="DD1317.*LAB2.*${current}"

# datorprov.sh caches results in a file named after the course regex, so clean
# with exactly the regex we report with. Otherwise a second run reports from
# the first run's results.
datorprov="$(dirname "$0")/datorprov/datorprov.sh"
# datorprov.sh is tangled from datorprov.sh.nw and not tracked; rebuild it so
# that we never run a copy older than the source.
make -s -C "$(dirname "${datorprov}")" datorprov.sh >/dev/null || exit 1
datorprov_regex="(${NEW_DATORPROV_COURSES}|${NEW_DATORPROV_EXAMROOMS})"
bash "${datorprov}" "${datorprov_regex}" clean
bash "${datorprov}" "${datorprov_regex}" rapportera

datorprov_courses="DD1317.*LAB2.*${current}"

# rapportera has just set grades, so read them from Canvas, not the cache.
canvaslms --refresh-cache results -c "$NEW_DATORPROV_COURSES" -A "LAB2" \
| sed -E "s/ ?[HV]T[0-9]{2}( \(.*\))?//" \
| ladok report -fv
