#!/bin/bash
for ((x=1; x<=10; x++))
do
    for ((y=1; y<=2000; y++))
    do
        rmdir "domek_grzybowski_$y"
    done
    cd ..

done