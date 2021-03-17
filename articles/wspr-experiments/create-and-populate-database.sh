#!/bin/bash -e

sqlite3 wsprspots.db < sqlite3db.sql

datafile="data"
dbscript=".temporarydbscript.sql"
subset="UNKNOWN"

if [ -e $dbscript ] ; then
  rm -f $dbscript
fi
trap "rm -f $dbscript" EXIT

echo "Generating db script..."
cat $datafile | while read line ; do
  if [[ $line == "" || $line == \#\#* ]]; then
    continue
  fi
  if [[ $line == \#\ * ]]; then
    subset=$(echo "$line" | awk '{ for (i=2; i<NF; i++) printf $i " "; print $NF; }')
  else
    echo "$line" | awk '{ printf "%sT%s %f %f %s %f\n", $1, $2, $5, $8, $9, $11 ; }' | while read dt snr pwr qrz km ; do
      echo "insert into wsprspots (dt, subset, qrz, snr, pwr, km) values (\"$dt\", \"$subset\", \"$qrz\", $snr, $pwr, $km);" >> $dbscript
    done
  fi
done

echo "Populating database..."

sqlite3 wsprspots.db < $dbscript

echo "See queries.sql for examples."
