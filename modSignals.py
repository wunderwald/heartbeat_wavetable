import math

def repeat(signal, numRepeats):
    out = []
    for i in range(numRepeats):
        for sample in signal:
            out.append(sample)
    return out

def normalize(signal):
    amp = max(abs(signal))
    factor = 1/amp
    out = []
    for sample in signal:
        out.append(sample * factor)
    return out

def scale(signal, factor):
    out = []
    for sample in signal:
        out.append(sample * factor)
    return out

def toInt(signal):
    out=[]
    for sample in signal:
        out.append(math.floor(sample))
    return out