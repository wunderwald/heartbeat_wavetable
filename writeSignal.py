import wave, struct

def writeSignal(signal, path, samplingRate):
    out = wave.open(path, mode='wb')
    out.setframerate(framerate=samplingRate)
    out.setnchannels(1)
    out.setsampwidth(2)
    for sample in signal:
        bytes = struct.pack('<h', sample)
        out.writeframesraw(bytes)
    out.close()