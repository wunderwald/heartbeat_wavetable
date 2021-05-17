import pandas as pd
import neurokit2 as nk

def extractEcgPeriods(path, samplingRate):
    ecgRaw = pd.read_csv(path, names=['ecg'])['ecg']
    ecgClean = nk.ecg_clean(ecgRaw, sampling_rate=samplingRate, method="neurokit")
    peaks = nk.ecg_findpeaks(ecgClean, sampling_rate=samplingRate, method="neurokit")
    rPeaks = peaks['ECG_R_Peaks']

    periods = []
    for i in range(1, len(rPeaks)):
        startIndex = rPeaks[i-1]
        endIndex = rPeaks[i]
        period = ecgClean[startIndex:endIndex]
        periods.append(period)
    return periods
