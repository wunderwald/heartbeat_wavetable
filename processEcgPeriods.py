import neurokit2 as nk
import modSignals as ms
import math

samplingRateAudio = 44100.
frequencyMiddleC = 261.625565

samplePeriodAudio = 1/samplingRateAudio
periodMiddleC = 1/frequencyMiddleC

# number of samples (at 44.1khz) for one period of a c note
numSamplesMiddleC = math.floor(periodMiddleC / samplePeriodAudio)

targetAmplitude = 32767

# input: one period of a ecg rcording => tune to middle c, normalize and scale it
def processEcgPeriod(period, samplingRateEcg, samplingRateAudio):
    signal = period
    signalResampled = nk.signal_resample(
        signal=signal,
        desired_length=numSamplesMiddleC,
        sampling_rate=samplingRateEcg,
        desired_sampling_rate=samplingRateAudio,
        method='interpolation'
    )
    signalScaled = ms.toInt(ms.scale(ms.normalize(signal=signalResampled), factor=targetAmplitude))
    return signalScaled

def processEcgPeriods(periods, samplingRateEcg, samplingRateAudio):
    out = []
    for period in periods:
        out.append(processEcgPeriod(period, samplingRateEcg, samplingRateAudio))
    return out