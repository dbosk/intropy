#!/bin/bash
set -a; source ~/.credentials; set +a
for i in $(seq 1 20); do
  out=$(scholar llm classify flipped-classroom-learning -n 50 --no-examples -t supports-claim -t refutes-claim -t qualifies-claim -t adjacent-subtopic -t off-topic-false-hit 2>&1)
  echo "$out" | tail -4
  echo "$out" | grep -q "Pending: 0" && break
  echo "$out" | grep -qi "no pending" && break
done
echo CLASSIFY-DONE
