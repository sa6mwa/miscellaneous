package hamcalc

import (
	"io"
	"text/template"
)

var slimjimtext = `G2BCX SLIM JIM FOR {{ .QRGMHz }} MHz
Velocity factor for radiating 1/2 wave = {{ .VelocityFactorRadiatingElement }}
Velocity factor for 1/4 wave stub = {{ .VelocityFactorLadderLine }}
          .---.                   .
          |<F>|                   | J POLE VERSION
          |   |                   | (ignore E, AJ = AS-E or B+C)
          |   |B (1/2 wave)       |
          |   |                   | B (1/2 wave element)
       AS |   |                   | AJ (overall length)
 (overall |   |                   |
  length) |     E (gap = A-B-C)   |
          |   |                   |   |
          |   |C (1/4 wave)       |   | C (1/4 wave)
          L D S                   L D S
          | | |                   | | |
          '-|-'                   '-|-'
            | D=50 ohm feed point   |
            O <-- RF choke          O
            |                       |
  L = lead, inner conductor of coax
  S = shield of coax
  D = length from bottom where to solder L and S (match point)

  AS = {{ printf "%.2f" .TotalLengthSlimjim }} cm              AJ = {{ printf "%.2f" .TotalLengthJPole }} cm
  B = {{ printf "%.2f" .HalfwaveSectionB }} cm
  C = {{ printf "%.2f" .QuarterwaveSectionC }} cm
  D = {{ printf "%.2f" .FeedpointD }} cm
  E = {{ printf "%.2f" .GapE }} cm
  F = {{ printf "%.2f" .DistanceBetweenSectionsF }} cm (not critical, can be ignored, works anyway)

  Pipe/wire total length = {{ printf "%.2f" (add .QuarterwaveMaterialLength .HalfwaveSectionB) }} cm
  Quarter wave material length = {{ printf "%.2f" .QuarterwaveMaterialLength }} cm
  Half wave material length = {{ printf "%.2f" .HalfwaveSectionB }} cm
`

var slimjimtemplate = template.Must(template.New("slimjim").Funcs(template.FuncMap{
	"add": func(val ...float64) float64 {
		var result float64
		for _, v := range val {
			result += v
		}
		return result
	},
}).Parse(slimjimtext))

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

// NewSlimJim returns a new SlimJim instance with defaults.
func NewSlimJim() *SlimJim {
	return &SlimJim{
		VelocityFactorLadderLine:       0.957,
		VelocityFactorRadiatingElement: 0.957,
	}
}

// SetVelocityFactor sets the velocity factors for the ladderline and
// radiating element in the SlimJim instance. Returns the input
// receiver object.
func (s *SlimJim) SetVelocityFactor(vfLadderline, vfRadiatingElement float64) *SlimJim {
	s.VelocityFactorLadderLine = vfLadderline
	s.VelocityFactorRadiatingElement = vfRadiatingElement
	return s
}

// Calculate performs the antenna calculations and fills in all fields
// in the SlimJim instance.
func (s *SlimJim) Calculate(mhz float64) *SlimJim {
	s.QRGMHz = mhz
	s.TotalLengthSlimjim = 22500*s.VelocityFactorLadderLine/s.QRGMHz + 300/s.QRGMHz
	s.TotalLengthJPole = (30000 * (0.5 * s.VelocityFactorRadiatingElement) / s.QRGMHz) + (30000 * (0.25 * s.VelocityFactorLadderLine) / s.QRGMHz)
	s.HalfwaveSectionB = 30000 * (0.5 * s.VelocityFactorLadderLine) / s.QRGMHz
	s.QuarterwaveSectionC = 30000 * (0.25 * s.VelocityFactorLadderLine) / s.QRGMHz
	s.FeedpointD = 30000 * (0.025 * s.VelocityFactorLadderLine) / s.QRGMHz
	s.GapE = 300 / s.QRGMHz
	s.DistanceBetweenSectionsF = 30000 * 0.02175 / s.QRGMHz
	s.QuarterwaveMaterialLength = (s.QuarterwaveSectionC * 2) + s.DistanceBetweenSectionsF
	return s
}

// DrawAntenna prints the blue print how to design the slimjim or
// J-pole antenna with all measurements. Calculate need to be called
// before DrawAntenna.
func (s *SlimJim) DrawAntenna(w io.Writer) error {
	return slimjimtemplate.Execute(w, s)
}
