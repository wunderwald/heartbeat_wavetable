import math
from generateSine import generateSine
from writeSignal import writeSignal
from extractEcgPeriods import extractEcgPeriods
import matplotlib.pyplot as plt
import neurokit2 as nk
import modSignals as ms

samplingRateAudio = 44100.
frequencyMiddleC = 261.625565

samplePeriodAudio = 1/samplingRateAudio
periodMiddleC = 1/frequencyMiddleC

# number of samples (at 44.1khz) for one period of a c note
numSamplesMiddleC = math.floor(periodMiddleC / samplePeriodAudio)

targetAmplitude = 32767

# testSignal = generateSine(samplesPerPeriod=numSamplesMiddleC, numPeriods=1000, amp=targetAmplitude)
# path = './sin.wav'
# writeSignal(signal=testSignal, path=path, samplingRate=samplingRateAudio)

# read periods from ecg 
ecgPath = './ecgData/crc1.csv'
samplingRateEcg = 1000
periods = extractEcgPeriods(path=ecgPath, samplingRate=samplingRateEcg)

signal = periods[2]
signalResampled = nk.signal_resample(
    signal=signal,
    desired_length=numSamplesMiddleC,
    sampling_rate=samplingRateEcg,
    desired_sampling_rate=samplingRateAudio,
    method='interpolation'
)

signalScaled = ms.toInt(ms.scale(ms.normalize(signal=signalResampled), factor=targetAmplitude))
signalRepeated = ms.repeat(signalScaled, 1000)

path='./ecg.wav'
writeSignal(signal=signalRepeated, path=path, samplingRate=samplingRateAudio)


