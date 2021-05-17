import math
from generateSine import generateSine
from writeSignal import writeSignal
from extractEcgPeriods import extractEcgPeriods
import matplotlib.pyplot as plt
import modSignals as ms
from processEcgPeriods import processEcgPeriods

samplingRateAudio=44100

# read periods from ecg 
ecgPath = './ecgData/crc1.csv'
samplingRateEcg = 1000
periods = extractEcgPeriods(path=ecgPath, samplingRate=samplingRateEcg)
waves = processEcgPeriods(periods=periods, samplingRateEcg=samplingRateEcg, samplingRateAudio=samplingRateAudio)

signal = ms.concat(waves)

path='./ecgs.wav'
writeSignal(signal=signal, path=path, samplingRate=samplingRateAudio)


