Assistente de Voz com Transcrição e Resposta de IA
Descrição do Projeto

Este projeto implementa um assistente virtual de voz, capaz de:

Gravar áudio do usuário pelo microfone.
Transcrever a fala em texto usando o modelo Whisper da OpenAI.
Enviar a pergunta para um modelo de linguagem local (Ollama - phi3:mini) para gerar uma resposta inteligente.
Exibir a resposta no terminal e, opcionalmente, reproduzir a resposta em áudio.

O objetivo é criar um assistente interativo que combina reconhecimento de voz, processamento de linguagem natural e síntese de voz, funcionando inteiramente local.

Funcionalidades
Gravação de áudio: Captura a fala do usuário via microfone com sounddevice.
Transcrição automática: Converte o áudio gravado em texto com whisper.
Resposta de IA: Envia o texto para o modelo phi3:mini do Ollama para gerar respostas contextuais.
Interatividade: Permite múltiplas interações no mesmo terminal.
Avisos claros: Notifica o usuário se não houver áudio detectado ou se houver erro de comunicação com a IA.
Requisitos
Python 3.11+
Bibliotecas Python:
sounddevice
numpy
scipy
whisper
subprocess (nativo do Python)
Ollama instalado e rodando (phi3:mini ou outro modelo leve)
Sistema com microfone funcional

Observação: PCs com pouca memória podem não suportar modelos grandes como llama3. Use modelos mais leves como phi3:mini.

Estrutura do Projeto
DIO-teste-com-audio/
│
├─ assistente.py          # Script principal do assistente
├─ gravacao.wav           # Arquivo de áudio temporário gerado pelo assistente
├─ README.md              # Este arquivo
├─ requirements.txt       # Lista de dependências Python
└─ venv/                  # Ambiente virtual Python
Como Rodar
Clone o repositório:
git clone <url-do-repositorio>
cd DIO-teste-com-audio
Ative o ambiente virtual:
# Windows PowerShell
.\venv\Scripts\Activate.ps1
Instale as dependências:
pip install -r requirements.txt
Garanta que o Ollama esteja rodando:
ollama run phi3:mini
Execute o assistente:
python assistente.py
Pressione ENTER para começar a falar, espere a contagem regressiva e fale a pergunta.
Possíveis Melhorias Futuras
Síntese de voz: Integrar gTTS ou outro motor TTS para reproduzir a resposta.
Interface gráfica: Criar uma interface simples para usuários iniciantes.
Suporte a múltiplos idiomas: Adicionar detecção de idioma e tradução.
Controle de fluxo de gravação: Ajustar tempo de gravação para permitir fala natural.
Observações
Alguns erros podem ocorrer se o Ollama não estiver rodando ou se houver conflito de porta (127.0.0.1:11434).
PCs com pouca memória podem precisar de modelos mais leves (phi3:mini) em vez de llama3.
A gravação de áudio é feita localmente, então não há envio de dados para a nuvem.
Créditos
Projeto desenvolvido por [Seu Nome] e equipe do curso DIO - Criando com IA.
Baseado em tecnologias Whisper (OpenAI) e Ollama AI.