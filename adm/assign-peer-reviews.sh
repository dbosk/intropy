#!/bin/bash

# This script assigns peer reviews to students in a course.

assign_peer_reviews() {
  url=$1
  curl -s -X POST \
    -d "authenticity_token=$CANVAS_TOKEN" \
    -d "peer_review_count=2" \
    -o /dev/null \
    ${url}/assign_peer_reviews
}

construct_assignment_url() {
  course_id=$1
  assignment_id=$2

  echo "https://${CANVAS_SERVER}/courses/${course_id}/assignments/${assignment_id}"
}

main() {
  course_id=$1
  assignment_id=$2

  url=$(construct_assignment_url ${course_id} ${assignment_id})
  assign_peer_reviews ${url}
}

main2() {
  URLs=$(canvaslms assignment -c prg[im]23 -a Laboration..[1245]. | \
    sed -En "/URL: https:/s|URL: (https://.*)$|\1|p")
  for url in ${URLs}
  do
    assign_peer_reviews ${url}
  done
}

main2
