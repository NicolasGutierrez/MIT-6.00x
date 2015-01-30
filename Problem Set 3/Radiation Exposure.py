def f(x):
    """
    This function describes the curve of radioactive activity of decaying Cobalt-60,
    which has a half-life of 5.27 years.
    Initial activity is 10 MBq.
    """
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start,stop,step):
    """
    Arguments:
        start: float, the time radiation exposure starts, measured in years.
        stop: float, the time radiation exposure ends, measured in years.
        step: float, the infinitessimal time-step to be used for integration.
    Returns:
        exposure: float, the total resulting radiation exposure, measured in MBq-
    """
    time = start
    exposure = 0
    while time < stop:
        exposure += f(time) * step
        time += step
    return exposure

# Random test    
print radiationExposure(3.00,10.32,0.0001)