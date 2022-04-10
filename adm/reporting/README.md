# Reporting from Canvas to LADOK

To report results from Canvas to LADOK we can run the following script:
```bash
#!/bin/bash

. ${HOME}/.profile

year=22
courses="DD13(10HT${year}3|17HT${year}1?)"
components="(LAB[123]|MAT1|KAL1)"

canvaslms results -c "$courses" -A "$components" | \
  sed -E "s/[HV]T${year}[0-9]?//" | \
  ladok report -fv
```

This requires the `canvaslms` and `ladok3` Python packages:
```bash
python3 -m pip install --upgrade canvaslms ladok3
canvaslms login
ladok login
```
