import sounddevice as sd
import scipy.io.wavfile as wav
import whisper

fs = 44100
seconds = 5

print("Gravando...")
audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()

wav.write("gravacao.wav", fs, audio)

model = whisper.load_model("base")
result = model.transcribe("gravacao.wav")

print(result["text"])
