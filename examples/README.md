# Examples

## Ex_DC1_VOLTAGE.fld

Ansys Maxwell 3D DC Conduction Voltage output.

`Grid Output Min: [-0.8mm -2.1mm 0mm] Max: [2mm 2.1mm 0.2mm] Grid Size: [0.1mm 0.1mm 0.1mm] `

Uses the built in example Ex_DC_1_DCconductionSolver. This can be opened via:

Open Examples -> Maxwell -> General -> DC Conduction -> Ex_DC_1_DCconductionSolver

Export;
```
.\fld2csv.py .\examples\Ex_DC1_VOLTAGE.fld
```


```
cat .\examples\Ex_DC1_VOLTAGE.fld | .\fld2csv.py > Ex_DC_1_VOLTAGE.csv
```
## TL071_BASSCUT.txt

NI ELVISmx Bode Analysis tool output.

$R_f = 10k\Omega$

$R_1 = 2.2k\Omega$

$C=1\mu F$

Rail voltages of $\pm$ 15v. Parameters 
F(START)=5 Hz
F(STOP)=20 kHz (myDAQ maximum)
Steps: 10/decade
V(PP) = 1

Export:
```
.\fld2csv.py .\examples\TL071_BASSCUT.txt -t elvis
```

```
cat .\examples\TL071_BASSCUT.txt | .\fld2csv.py > TL071_BASSCUT.csv
```