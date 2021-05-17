import math
from generateSine import generateSine
from writeSignal import writeSignal

samplingRateAudio = 44100.
frequencyMiddleC = 261.625565

samplePeriodAudio = 1/samplingRateAudio
periodMiddleC = 1/frequencyMiddleC

# number of samples (at 44.1khz) for one period of a c note
numSamplesMiddleC = math.floor(periodMiddleC / samplePeriodAudio)

targetAmplitude = 32767

testSignal = generateSine(samplesPerPeriod=numSamplesMiddleC, numPeriods=1000, amp=targetAmplitude)

path = './sin.wav'
writeSignal(signal=testSignal, path=path, samplingRate=samplingRateAudio)
