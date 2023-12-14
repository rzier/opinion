#!/bin/bash


mkdir "../data/$1"
./fetch_utube.py $1 0 
./get_csv.py $1
./vinfo.py $1
./analysis.py $1
