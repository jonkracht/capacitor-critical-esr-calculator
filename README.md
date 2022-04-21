# capacitor-critical-esr-calculator
Compute ESR value where capacitor is likely faulty

Capacitors are characterized by their capacitance and operating voltage.  By measuring the capacitor's equivalent series resistance (ESR) (for example, manufactured by [Peak Electronics](https://www.peakelec.co.uk/acatalog/esr70-capacitor-esr-meter.html)), it may be determined either properly functioning or faulty.

Critical ESR value are tabulated at discrete values of capacitance and voltage.  This calculator employs linear interpolation to compute critical ESR at arbitrary values in the range of the provided data.  
    * Voltage:  6.3V to 630V  
    * Capacitance:  4.7 $\mu$F to 22mF
