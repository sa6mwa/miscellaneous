# Fix invisible checkboxes

Background: Checkboxes are invisible in Ubuntu Mate since fldigi uses gtk+ by
default. Some FLTK applications support the `-scheme` command line option:

```
flmsg -scheme base
flmsg -scheme plastic
```

fldigi has to be configured from within via menu path:
> Configure / UI / General.

Choose UI scheme (base is probably the best option).
