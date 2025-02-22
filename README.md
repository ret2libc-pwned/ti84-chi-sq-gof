# TI-84 $\chi^2\texttt{test-GOF}$ Python
An alternative to the buggy TI-84 Calculator's built-in chi-square($\chi^2$) GOF test written in Python.

This script uses Monte Carlo algorithm to estimate probability density function for $\chi^2$ distribution and it will output an estimated $P$ value. 

## Installation
The program is designed for `TI-84 Plus CE Python` calculators. 

1. Download the file `main.py`.
2. Install `TI Connect CE` on your device.
3. Connect your calculator via USB cable.
4. Select the file manager icon on the left pane, then drag the file to the right part of the window.
5. Run the program on your calculator's Python app.

## Configuration
You can change the number of iterations by modifying `SIMULATIONS` variable if the calculation is too slow.

Also, you may abort the program after it outputs the $\chi^2$ statistic then use the calculator's built-in $\chi^2\texttt{cdf}$ function to calculate the $P$ value.
