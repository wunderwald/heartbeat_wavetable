import struct
import wave
import math
from generateSine import generateSine

samplingRateAudio = 44100.

frequencyMiddleC = 261.625565

samplePeriodAudio = 1/samplingRateAudio
periodMiddleC = 1/frequencyMiddleC

# number of samples (at 44.1khz) for one period of a c note
numSamplesMiddleC = math.floor(periodMiddleC / samplePeriodAudio)

amp = 32767

testSignal = generateSine(numSamplesMiddleC, 1000, 2000)

out = wave.open('./test.wav', mode='wb')
out.setframerate(framerate=samplingRateAudio)
out.setnchannels(1)
out.setsampwidth(2)
for sample in testSignal:
    bytes = struct.pack('<h', sample)
    out.writeframesraw(bytes)
out.close()