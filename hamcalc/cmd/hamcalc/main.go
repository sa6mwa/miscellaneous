package main

import (
	"flag"
	"fmt"
	"os"
	"path"

	"github.com/sa6mwa/miscellaneous/hamcalc"
)

const (
	SLIMJIM string = "slimjim"
)

const (
	helpMsg string = `Usage: %s command [options/variables...]

COMMANDS
slimjim     Calculate a resonant Slimjim or J-Pole antenna from frequency
            as input.
`
	slimjimHelpMsg string = `Usage: %s slimjim [options] MHz
MHz is floating point and mandatory (e.g 444.83125).
`
)

var (
	slimjimCmd = flag.NewFlagSet(SLIMJIM, flag.ExitOnError)

	slimjimVFL = hamcalc.NewSlimJim().VelocityFactorLadderLine
	slimjimVFR = hamcalc.NewSlimJim().VelocityFactorRadiatingElement
)

func init() {
	slimjimCmd.Float64Var(&slimjimVFL, "vfl", hamcalc.NewSlimJim().VelocityFactorLadderLine, "Ladderline velocity factor")
	slimjimCmd.Float64Var(&slimjimVFR, "vfr", hamcalc.NewSlimJim().VelocityFactorRadiatingElement, "Velocity factor of radiating element")

	flag.Usage = func() {
		fmt.Fprintf(flag.CommandLine.Output(), helpMsg, path.Base(os.Args[0]))
		flag.PrintDefaults()
	}
	slimjimCmd.Usage = func() {
		fmt.Fprintf(slimjimCmd.Output(), slimjimHelpMsg, path.Base(os.Args[0]))
		slimjimCmd.PrintDefaults()
	}
}

func main() {
	flag.Parse()

	args := flag.Args()
	if len(args) < 1 {
		flag.Usage()
		os.Exit(1)
	}

	switch args[0] {
	case SLIMJIM:
		slimjimCmd.Parse(args[1:])
		args := slimjimCmd.Args()
		if len(args) < 1 {
			fmt.Fprintln(slimjimCmd.Output(), "Syntax error: missing mandatory variable, see -h for help")
			os.Exit(1)
		}
		var mhz float64
		if _, err := fmt.Sscanf(slimjimCmd.Arg(0), "%f", &mhz); err != nil {
			fmt.Println("Error:", err)
			os.Exit(1)
		}

		sj := hamcalc.NewSlimJim().SetVelocityFactor(slimjimVFL, slimjimVFR).Calculate(mhz)
		if err := sj.DrawAntenna(os.Stdout); err != nil {
			panic(err)
		}
	default:
		flag.Usage()
		os.Exit(1)
	}
}
