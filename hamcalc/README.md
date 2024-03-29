<!-- Code generated by gomarkdoc. DO NOT EDIT -->

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


# hamcalc

```go
import "github.com/sa6mwa/miscellaneous/hamcalc"
```

hamcalc contains a set of amateur radio and antenna related calculators.

## Index

- [type SlimJim](<#type-slimjim>)
  - [func NewSlimJim() *SlimJim](<#func-newslimjim>)
  - [func (s *SlimJim) Calculate(mhz float64) *SlimJim](<#func-slimjim-calculate>)
  - [func (s *SlimJim) DrawAntenna(w io.Writer) error](<#func-slimjim-drawantenna>)
  - [func (s *SlimJim) SetVelocityFactor(vfLadderline, vfRadiatingElement float64) *SlimJim](<#func-slimjim-setvelocityfactor>)


## type SlimJim

```go
type SlimJim struct {
    QRGMHz                         float64
    VelocityFactorRadiatingElement float64
    VelocityFactorLadderLine       float64
    TotalLengthSlimjim             float64 // cm
    TotalLengthJPole               float64 // cm
    HalfwaveSectionB               float64 // cm
    QuarterwaveSectionC            float64 // cm
    FeedpointD                     float64 // cm
    GapE                           float64 // cm
    DistanceBetweenSectionsF       float64 // cm
    QuarterwaveMaterialLength      float64 // cm
}
```

### func NewSlimJim

```go
func NewSlimJim() *SlimJim
```

NewSlimJim returns a new SlimJim instance with defaults.

### func \(\*SlimJim\) Calculate

```go
func (s *SlimJim) Calculate(mhz float64) *SlimJim
```

Calculate performs the antenna calculations and fills in all fields in the SlimJim instance.

### func \(\*SlimJim\) DrawAntenna

```go
func (s *SlimJim) DrawAntenna(w io.Writer) error
```

DrawAntenna prints the blue print how to design the slimjim or J\-pole antenna with all measurements. Calculate need to be called before DrawAntenna.

### func \(\*SlimJim\) SetVelocityFactor

```go
func (s *SlimJim) SetVelocityFactor(vfLadderline, vfRadiatingElement float64) *SlimJim
```

SetVelocityFactor sets the velocity factors for the ladderline and radiating element in the SlimJim instance. Returns the input receiver object.



Generated by [gomarkdoc](<https://github.com/princjef/gomarkdoc>)
