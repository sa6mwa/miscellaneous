# Random wire lengths to avoid

## hwl.c

Compile like this...

```
gcc -o hwl hwl.c
```

## Generate data for Gnuplot

Run the binary (`hwl`) and direct output to file `f`...

```
./hwl > f
```

## Gnuplot

Run the following to make a gnuplot png called `g.png`...

```
gnuplot rw.gnu
```

## Or use fullrun.sh

There are two C files, `hwl.c` and `hwlspecial.c`. The *special* file is
specific for certain frequency ranges where the purpose is not disclosed. The
ranges are unclassified why it is included in this repository. By editing
`fullrun.sh` you can choose which code you want to use. `fullrun.sh` will
execute the commands above.

```
./fullrun.sh
```
