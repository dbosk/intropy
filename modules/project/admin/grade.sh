#!/bin/bash

COURSE="prg[im]2[2-9]"
ASSIGNM="Välj p-uppgift"
HANDINS="/tmp/prgim2x.puppg.handedin"
#HANDINS=$(mktemp)

get_row() {
  egrep "[^a-z]$1" $2
}

grade() {
  course="$(get_row $1 $HANDINS | cut -f 1)"
  echo "$course" "$1"
  canvaslms grade -c "$course" -a "$ASSIGNM" -u "$1" -g 'complete'
}

to_grade() {
  cat $HANDINS
}

grade_all() {
  for student in $(cut -f 3 $HANDINS); do
    grade $student
  done
  rm -Rf $HANDINS
}

update() {
  canvaslms submissions -lc "$COURSE" -a "$ASSIGNM" | \
    egrep "[0-9]{4}-[0-9]{2}-[0-9]{2}" | grep -v "complete" > $HANDINS
}

test -e $HANDINS || update

$*
