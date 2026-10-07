#!/bin/bash
# Runs every query on every live provider under one scholar session; logs counts.
set -a; source ~/.credentials; set +a
S=flipped-classroom-learning
OUT=/tmp/claude-1000/research-flipped/runs
L=50
declare -A Q
FC='("flipped classroom" OR "inverted classroom" OR "flipped learning")'
Q[S1]="$FC AND (meta-analysis OR \"systematic review\") AND (achievement OR \"learning outcomes\" OR performance)"
Q[S2]="$FC AND (programming OR \"computer science\" OR computing) AND (achievement OR \"learning outcomes\" OR performance OR grades)"
Q[C1]="$FC AND (meta-analysis OR \"systematic review\") AND (\"publication bias\" OR heterogeneity OR \"no significant difference\" OR moderator OR moderators OR limitations)"
Q[C2]="$FC AND (programming OR \"computer science\" OR computing) AND (\"no significant difference\" OR \"no difference\" OR challenges OR resistance OR negative)"
Q[P1]="($FC OR \"active learning\") AND (lecture OR lectures) AND (\"student perception\" OR \"student perceptions\" OR satisfaction OR preference OR preferences OR resistance OR \"feeling of learning\")"
declare -A D
D[S1]="flipped classroom meta-analysis"
D[S2]="flipped classroom programming"
D[C1]="flipped classroom systematic review"
D[C2]="flipped classroom computer science"
D[P1]="active learning lecture perception"
for k in S1 S2 C1 C2 P1; do
  q="${Q[$k]}"
  for p in openalex ieee; do
    scholar search "$q" -n $S -p $p -l $L -f csv > $OUT/$k-$p.csv 2> $OUT/$k-$p.err
  done
  scholar search "TS=($q)" -n $S -p wos -l $L -f csv > $OUT/$k-wos.csv 2> $OUT/$k-wos.err
  scholar search "TITLE-ABS-KEY($q)" -n $S -p scopus -l $L -f csv > $OUT/$k-scopus.csv 2> $OUT/$k-scopus.err
  scholar search "${D[$k]}" -n $S -p dblp -l $L -f csv > $OUT/$k-dblp.csv 2> $OUT/$k-dblp.err
done
for f in $OUT/*.csv; do echo "$(basename $f .csv) $(grep "^# Results" $f)"; done
grep -l . $OUT/*.err | while read e; do echo "== $e"; tail -3 $e; done
