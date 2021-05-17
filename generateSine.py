import math

def generateSine(samplesPerPeriod, numPeriods, amp):
    signal = []
    for i in range(samplesPerPeriod * numPeriods):
        sample = math.floor(math.sin((i%samplesPerPeriod)/samplesPerPeriod * math.pi * 2) * amp)
        signal.append(sample)
    return signal
