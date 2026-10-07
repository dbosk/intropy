#!/bin/bash
# Round 2: computing-specific reviews and perceived vs actual learning.
set -a; source ~/.credentials; set +a
S=flipped-classroom-learning
OUT=/tmp/claude-1000/research-flipped/runs
L=50
declare -A Q
FC='("flipped classroom" OR "inverted classroom" OR "flipped learning")'
Q[S3]="$FC AND (programming OR \"computer science\" OR computing) AND (meta-analysis OR \"systematic review\" OR \"literature review\")"
Q[C3]="$FC AND (programming OR \"computer science\" OR computing) AND (meta-analysis OR \"systematic review\" OR \"literature review\") AND (\"no significant difference\" OR heterogeneity OR limitations OR \"mixed results\")"
Q[P2]="($FC OR \"active learning\") AND (\"perceived learning\" OR \"feeling of learning\" OR \"self-reported learning\") AND (lecture OR lectures OR passive)"
declare -A D
D[S3]="flipped classroom programming review"
D[C3]="flipped classroom computing review"
D[P2]="feeling of learning active"
for k in S3 C3 P2; do
  q="${Q[$k]}"
  for p in openalex ieee; do
    scholar search "$q" -n $S -p $p -l $L -f csv > $OUT/$k-$p.csv 2> $OUT/$k-$p.err
  done
  scholar search "TS=($q)" -n $S -p wos -l $L -f csv > $OUT/$k-wos.csv 2> $OUT/$k-wos.err
  scholar search "TITLE-ABS-KEY($q)" -n $S -p scopus -l $L -f csv > $OUT/$k-scopus.csv 2> $OUT/$k-scopus.err
  scholar search "${D[$k]}" -n $S -p dblp -l $L -f csv > $OUT/$k-dblp.csv 2> $OUT/$k-dblp.err
done
for k in S3 C3 P2; do for f in $OUT/$k-*.csv; do echo "$(basename $f .csv) $(grep "^# Results" $f)"; done; done
grep -h WARNING $OUT/S3-* $OUT/C3-* $OUT/P2-* | sort | uniq -c
