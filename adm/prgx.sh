#!/bin/bash

# Report LAB2
#
# Usage:
#   prgx.sh            rapportera, then report to Ladok
#   prgx.sh COMMAND    run a datorprov.sh command (P, ickeP, all, clean, ...)
#                      on the same courses, and so on the same cached results
#
# Explore with prgx.sh COMMAND first; prgx.sh then reports exactly the cached
# results you looked at. Run prgx.sh clean yourself to fetch new results.
# DRY_RUN=1 prints the Canvas writes and the Ladok rows instead of sending them.

#NEW_DATORPROV_COURSES="(prgm(2[4-9]|[3-9][0-9])|DD1317 HT(2[5-9]|[3-9][0-9]))"
NEW_DATORPROV_COURSES="(DD1317 HT(2[5-9]|[3-9][0-9]))"
current=$(date +%Y-%m)
#NEW_DATORPROV_EXAMROOMS="DD131[07] LAB2.*${current}"
NEW_DATORPROV_EXAMROOMS="DD1317.*LAB2.*${current}"

datorprov="$(dirname "$0")/datorprov/datorprov.sh"
# datorprov.sh is tangled from datorprov.sh.nw and not tracked; rebuild it so
# that we never run a copy older than the source.
make -s -C "$(dirname "${datorprov}")" datorprov.sh >/dev/null || exit 1
datorprov_regex="(${NEW_DATORPROV_COURSES}|${NEW_DATORPROV_EXAMROOMS})"

if [ $# -gt 0 ]; then
  exec bash "${datorprov}" "${datorprov_regex}" "$@"
fi

bash "${datorprov}" "${datorprov_regex}" rapportera

datorprov_courses="DD1317.*LAB2.*${current}"

# rapportera has just set grades, so read them from Canvas, not the cache.
canvaslms --refresh-cache results -c "$NEW_DATORPROV_COURSES" -A "LAB2" \
| sed -E "s/ ?[HV]T[0-9]{2}( \(.*\))?//" \
| if [ "${DRY_RUN:-0}" = "1" ]; then
    echo "DRY_RUN: would send these rows to ladok report -fv:" >&2
    cat
  else
    ladok report -fv
  fi
