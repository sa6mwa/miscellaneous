# hamcalc

`hamcalc` is a small CLI with a selection of various amateur radio and antenna
related calculators.

```
$ go run github.com/sa6mwa/miscellaneous/hamcalc/cmd/hamcalc -h
Usage: hamcalc command [options/variables...]

COMMANDS
slimjim     Calculate a resonant Slimjim or J-Pole antenna from frequency
            as input.
```

## Installation

```console
go install github.com/sa6mwa/miscellaneous/hamcalc/cmd/hamcalc@latest

# or...

go build -o hamcalc github.com/sa6mwa/miscellaneous/hamcalc/cmd/hamcalc@latest
sudo install hamcalc /usr/local/bin/
```


