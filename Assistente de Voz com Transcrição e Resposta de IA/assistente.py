import subprocess
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import whisper
import time
from gtts import gTTS
import os
import tempfile
import platform

# Configurações
DURACAO = 5  # segundos de gravação
FS = 44100   # taxa de amostragem

def gravar_audio():
    input("Pressione ENTER e prepare-se para falar...")
    print(f"🎤 Gravando em {DURACAO} segundos...")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    audio = sd.rec(int(DURACAO * FS), samplerate=FS, channels=1, dtype=np.int16)
    sd.wait()
    wav.write("gravacao.wav", FS, audio)
    print("🔴 Gravação finalizada!")
    return "gravacao.wav"

def transcrever_audio(caminho_audio):
    print("🧠 Transcrevendo áudio...")
    model = whisper.load_model("base")
    result = model.transcribe(caminho_audio)
    texto = result["text"].strip()
    if not texto:
        print("⚠️ Nenhum áudio detectado. Tente falar mais alto ou mais claro.")
        return None
    print(f"Você disse: {texto}")
    return texto

def perguntar_ollama(pergunta):
    try:
        comando = ["ollama", "run", "phi3:mini"]
        resultado = subprocess.run(
            comando,
            input=pergunta,
            text=True,
            capture_output=True,
            encoding='utf-8',  # força UTF-8 para evitar UnicodeDecodeError
            errors='ignore'
        )
        if resultado.returncode != 0:
            raise Exception(resultado.stderr.strip())
        resposta = resultado.stdout.strip()
        if not resposta:
            return "❌ Nenhuma resposta do Ollama"
        return resposta
    except Exception as e:
        return f"❌ Erro ao se comunicar com Ollama: {e}"

def falar_texto(texto):
    try:
        tts = gTTS(texto, lang='pt')
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
            caminho_audio = tmpfile.name
        tts.save(caminho_audio)
        print("🔊 Reproduzindo resposta...")
        if platform.system() == "Windows":
            os.system(f'start /min "" "{caminho_audio}"')
        else:
            # Linux / macOS
            os.system(f"mpg123 '{caminho_audio}'")
    except Exception as e:
        print(f"⚠️ Não foi possível reproduzir o áudio: {e}")

def main():
    print("Carregando modelo Whisper...")
    try:
        while True:
            caminho = gravar_audio()
            texto = transcrever_audio(caminho)
            if texto:
                resposta = perguntar_ollama(texto)
                print(f"💬 Resposta: {resposta}")
                falar_texto(resposta)
            print("\n---\n")
    except KeyboardInterrupt:
        print("Assistente finalizado pelo usuário.")

if __name__ == "__main__":
    main()