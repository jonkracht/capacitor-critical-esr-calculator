import numpy as np
from scipy import interpolate

def makeInterpolation():
    '''Function to create interpolation from table of discrete data'''

    # Voltages (in Volts) and capacitances (in microfarads) at which ESR is measured (in Ohms)
    v = np.array([6.3, 10, 16, 25, 35, 50, 63, 100, 160, 250, 400, 630])
    c = np.array([4.7, 10, 22, 47, 100, 220, 470, 1000, 2200, 4700, 10000, 22000])
    esr = np.array([[62, 54, 45, 40, 34, 28, 25, 23, 19, 16, 13, 11],
                [29, 25, 21, 19, 16, 13, 12, 11, 8.7, 7.4, 6.2, 5.2],
                [13, 11, 9.6, 8.4, 7.2, 6.0, 5.4, 4.8, 4.0, 3.4, 2.8, 2.4],
                [6.2, 5.4, 4.5, 4.0, 3.4, 2.8, 2.5, 2.3, 1.9, 1.6, 1.3, 1.1],
                [2.9, 2.5, 2.1, 1.9, 1.6, 1.3, 1.2, 1.1, .87, .74, .62, .52],
                [1.3, 1.1, .97, .84, .72, .6, .54, .48, .40, .34, .28, .24],
                [0.62, .54, .45, .4, .34, .28, .25, .23, .19, .16, .13, .11],
                [.29, 25, .21, .19, .16, .13, .12, .11, .09, .07, .06, .05],
                [.16, .14, .12, .11, .10, .09, .08, .07, .06, .06, .05, .04],
                [.09, .08, .07, .06, .05, .05, .05, .04, .04, .04, .04, .03],
                [.06, .05, .05, .05, .04, .04, .04, .04, .03, .03, .03, .03],
                [.04, .04, .04, .04, .03, .03, .03, .03, .03, .03, .03, .03]
                ])

    # Create function interpolating data
    return interpolate.interp2d(v, c, esr, kind='linear')


def queryUser():
    '''Get capacitance and voltage from user.'''

    print('\n*******************************************************')
    c = float(input('Enter capacitance [in microfarads]:  '))
    v = float(input('Enter voltage [in Volts]:  '))

    return c, v


def main():
    print('\n*** Capacitor calculator for critical values of ESR ***')

    thresholdESR = makeInterpolation()

    while True:
        capacitance, voltage = queryUser()

        print('\nCritical ESR:  ' + str(round(float(thresholdESR(voltage, capacitance)), 2)))

        if input('\nAgain?  (\'y\' for yes; anything else exits)  ').lower() != 'y':
            break

    return

if __name__ =='__main__':
    main()