# dB in GNU bc

```
bc -l
define log10 (x) { scale=5; return (10*l(x)/l(10)); }
log10(0.5)
-3.01027
```
