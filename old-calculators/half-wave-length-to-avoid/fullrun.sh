#!/bin/sh -xe
B=hwlspecial
gcc -o ${B} ${B}.c
./${B} > f
gnuplot rw.gnu
eom f.png
