#!/bin/bash
# usage: concepts/sheet.sh <episode id> <times...>  -> concepts/out/<id>/sheet.png (4 per row)
cd /home/user/FinancePros/engine; source env.sh
id=$1; shift; d=concepts/out/$id; ts=$(echo "$@" | tr ' ' ',')
EPF=concepts/episodes/$id.json; [ -f $EPF ] || EPF=concepts/episodes/auto/$id.json; REUSE=1 python concepts/build.py $EPF --stills $ts >/dev/null 2>&1
n=$#; ins=""; i=0; f=""
for t in "$@"; do ins="$ins -i $d/still-$t.png"; f="$f[$i]scale=380:-1[s$i];"; i=$((i+1)); done
row=""; rows=""; r=0
for i in $(seq 0 $((n-1))); do row="$row[s$i]"; if [ $(( (i+1) % 4 )) -eq 0 ] || [ $i -eq $((n-1)) ]; then k=$(( (i % 4) + 1 )); if [ $k -lt 4 ]; then for j in $(seq $k 3); do f="$f color=white:s=380x$( [ -n "$LAND" ] && echo 214 || echo 676)[p$r$j];"; row="$row[p$r$j]"; done; fi; f="$f${row}hstack=4[r$r];"; rows="$rows[r$r]"; r=$((r+1)); row=""; fi; done
if [ $r -gt 1 ]; then f="$f${rows}vstack=$r"; else f="${f%;}"; f="${f%\[r0\]}"; f="${f/hstack=4\[r0\]/hstack=4}"; fi
$FFMPEG -loglevel error -y $ins -filter_complex "$f" -frames:v 1 $d/sheet.png && echo $d/sheet.png
