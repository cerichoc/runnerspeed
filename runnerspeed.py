#/usr/bin/env python

import sys
import re
import math


def checktime(speedminkm, kilometers):

    val         = []
    timevalues  = [3600,60,1]

    for i,time in enumerate(timevalues):
        if i == 0:  value = (speedminkm*kilometers*60)
        else:       value = value -(val[i-1] * timevalues[i-1])
        val.append((int)(value/time))
        
    return val

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print "Please introduce three arguments: speed metric_unit (m/s, Km/h or min/Km)"
        print "Exemple: 12 Km/h"
        exit(-1)

    speed = float(sys.argv[1])

    if type(speed) != float:
        print "Second argument shall be the speed of the runner, please enter a number"
        exit(-1)

    units = sys.argv[2]
    units_ms = units_kmh = units_minkm = False

    if re.match(r'[Mm](.*)/(.*)[Ss]', units):
        units_ms = True
    elif re.match(r'[Kk]m(.*)/(.*)[Hh]', units):
        units_kmh = True
    elif re.match(r'[Mm]in(.*)/(.*)[Kk]m', units):
        units_minkm = True
    else:    
        print "Please introduce three arguments: speed metric_unit (m/s, Km/h or min/Km)"
        exit(-1)


    if units_ms == True:
        speed_kmh   = speed * (3600/1000)
        speed_minkm = 1/speed * (1000/60)
        speed_ms   = speed

    elif units_kmh == True:
        speed_ms    = (speed * 1000 * (1/3600))
        speed_minkm = (60/speed)
        speed_kmh   = speed

    elif units_minkm == True:
        speed_ms   = 1/speed * (1/60)
        speed_kmh  = 60/speed
        speed_minkm   = speed

    print speed_ms,"m/s"
    print speed_kmh,"Km/h"
    print speed_minkm,"min/Km"

  
    ten = 10
    val = checktime(speed_minkm, ten)
    print "Runner will run",ten,"km in",val[0],"h",val[1],"\"",val[2],"\'"
    
    semi = 21
    val = checktime(speed_minkm, semi)
    print "Runner will run",semi," km in",val[0],"h",val[1],"\"",val[2],"\'"

    marathon = 42
    val = checktime(speed_minkm, marathon)
    print "Runner will run",marathon," km in",val[0],"h",val[1],"\"",val[2],"\'"

