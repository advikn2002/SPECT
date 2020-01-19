# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd                         #import modules in python
import numpy 
from django.conf import settings as djangoSettings
from numpy.polynomial.polynomial import polyfit
import matplotlib.pyplot as plt

def start(n,xval=None,xFile='xSample.csv',yFile='ySample.csv'):

    xdata = pd.read_csv ( djangoSettings.MEDIA_ROOT + "/data/" + xFile , header = None )
    ydata = pd.read_csv ( djangoSettings.MEDIA_ROOT + "/data/" + yFile , header = None )
    # Sample data
    x=xdata[0]
    y=ydata[0]

        # print ( '1.curvefit\n2.value\n3.bar\n4.hist\n5.exit' )
        # n = int ( input ( 'choose option :3' ) )

    if n==0 :
        return 'blank.png'
    elif n == 1 :
        return curvefit( x , y )
    elif n == 2 :
        return value( x , y,xval)
    elif n == 3 :
        return bargraph( x , y )
    elif n == 4 :
        return histgraph( x , y )
    elif n==5:
       return scatter(x,y)


def curvefit(x,y):       #
    plt.clf()
        # Sample data for curve fit
   

    # Fit with polyfit
    b, m = polyfit(x, y, 1)

    plt.plot(x, y, 'o', color ='red', label ="data")
    plt.plot(x, b + m * x, '--', color ='blue', label ="optimized data")
    plt.title('SPECTRUM GRAPH')
    plt.xlabel('Absorbance')
    plt.ylabel('Concentration')
    plt.legend()
    plt.savefig(djangoSettings.MEDIA_ROOT+'/graphs/curvefit.png')
    return 'curvefit.png'
    
def histgraph(x,y):        #to plot histogram
    plt.clf()
    df=pd.DataFrame(y)
    plt.hist(df,bins=20)
    plt.savefig(djangoSettings.MEDIA_ROOT+'/graphs/hist.png')
    return 'hist.png'

def bargraph(x,y):          #to plot bargraph
    plt.clf()
    plt.bar(x,y)
    plt.xlabel('Absorbance')
    plt.ylabel('Concentration')
    plt.savefig ( djangoSettings.MEDIA_ROOT + '/graphs/bar.png' )
    return 'bar.png'


def value(x,y,xval):
    b, m = polyfit(x, y, 1)
    yval=b+m*xval
    return yval

def scatter(x,y):           #to plot scatter graph
    plt.clf()
    plt.scatter(x,y)
    plt.xlabel('Absorbance')
    plt.ylabel('Concentration')
    plt.savefig ( djangoSettings.MEDIA_ROOT + '/graphs/scatter.png' )
    return 'scatter.png'
    

        
         
