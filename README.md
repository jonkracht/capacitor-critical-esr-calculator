# capacitor-critical-esr-calculator

## Background

Equivalent series resistance (ESR) is a measurement that can help determine whether a capacitor is properly functioning.
When new, a capacitor's resistance is normally quite low and will, in time and with use, begin to increase.
When the ESR increases beyond some critical value, it will cease to function properly in-circuit, even though its measured capacitance may still be within spec.

To measure ESR, a specialized device is required, such as [Peak Electronics' Atlas ESR Gold](https://www.peakelec.co.uk/acatalog/esr70-capacitor-esr-meter.html)).
Once the capacitor's ESR has been measured, it may be compared to the threshold ESR value.
Peak Electronics provides threshold ESR for discrete values of capacitance and voltage:

![capacitor-threshold-esr.png](./capacitor-threshold-esr.png)

**Lower ESR is better.**

## Present work

The goal of this work is to compute threshold ESR for arbitary capacitance and voltage.
Two-dimensional interpolation is used.
As such, this tool should not be used much beyond the bounds of which data was collected (10-630V, 4.7 - 22000 $\mu F$).










