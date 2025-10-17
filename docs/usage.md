# 🎵 YT-Down - YouTube to MP3 Converter

Uma aplicação Python moderna e eficiente para baixar vídeos do YouTube e converter para MP3, com suporte a playlists e processamento paralelo.

## ✨ Características

- 📺 **Download de vídeos individuais** do YouTube
- 📋 **Download de playlists completas** com processamento paralelo
- 🎵 **Conversão automática para MP3** com qualidade configurável
- 🏷️ **Metadados ID3** automáticos (título, artista)
- 📊 **Barras de progresso** para acompanhar downloads
- ⚡ **Processamento concorrente** para máxima eficiência
- 🛡️ **Tratamento robusto de erros** e logging detalhado
- 🔧 **Interface CLI amigável** com validação de argumentos

## 🚀 Instalação Rápida

```bash
# Clone o repositório
git clone https://github.com/ozairx/yt-down.git
cd yt-down

# Instale as dependências com UV
uv sync

# Teste a instalação
uv run python main.py --help
```

## 💻 Uso

### Download de vídeo individual

```bash
# Download básico
uv run python main.py --url "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Com opções personalizadas
uv run python main.py --url "https://youtu.be/dQw4w9WgXcQ" \\
  --output-dir "./downloads" \\
  --quality 320 \\
  --format mp3 \\
  --verbose
```

### Download de playlist completa

```bash
# Download de playlist
uv run python main.py --playlist "https://www.youtube.com/playlist?list=PLiADrOnicrBsYIRoKizPIezNi5gDIZ2hO"

# Com processamento paralelo
uv run python main.py --playlist "https://www.youtube.com/playlist?list=PLiADrOnicrBsYIRoKizPIezNi5gDIZ2hO" \\
  --concurrent 5 \\
  --quality 256 \\
  --output-dir "./music"
```

### Opções disponíveis

| Opção | Descrição | Padrão |
|-------|-----------|--------|
| `-u, --url` | URL de vídeo individual do YouTube | - |
| `-p, --playlist` | URL de playlist do YouTube | - |
| `-o, --output-dir` | Diretório de saída | `./downloads` |
| `-q, --quality` | Qualidade do áudio em kbps | `192` |
| `-f, --format` | Formato de saída (mp3, wav, m4a) | `mp3` |
| `-c, --concurrent` | Downloads simultâneos | `3` |
| `-v, --verbose` | Logging detalhado | `false` |

## ⚙️ Configuração

### Variáveis de ambiente (.env)

```bash
# Copie o arquivo de exemplo
cp .env.example .env

# Edite conforme necessário
DOWNLOAD_DIR=./downloads
AUDIO_QUALITY=192
OUTPUT_FORMAT=mp3
MAX_CONCURRENT_DOWNLOADS=3
LOG_LEVEL=INFO
```

### Estrutura de saída

```bash
downloads/
├── Artista - Título do Vídeo.mp3
├── Outro Artista - Outro Título.mp3
└── temp/  # Arquivos temporários (limpos automaticamente)
```

## 🛠️ Desenvolvimento

### Comandos úteis

```bash
# Formatar código
uv run ruff format .

# Verificar problemas
uv run ruff check .

# Corrigir problemas automaticamente
uv run ruff check --fix .

# Executar aplicação
uv run python main.py [opcoes]
```

### Tarefas do VS Code

Use `Ctrl+Shift+P` → "Tasks: Run Task" para acessar:

- **uv: Install dependencies** - Instalar dependências
- **ruff: Check** - Verificar código
- **ruff: Format** - Formatar código
- **Run main.py** - Executar aplicação

## 🏗️ Arquitetura

```bash
src/yt_down/
├── __init__.py         # Módulo principal
├── cli.py             # Interface de linha de comando
├── app.py             # Orquestrador principal
├── config.py          # Gerenciamento de configuração
├── downloader.py      # Download do YouTube
├── converter.py       # Conversão para MP3
├── utils.py           # Validação de URLs
└── logger.py          # Sistema de logging
```

### Fluxo de processamento

1. **Validação** → Verifica URLs do YouTube
2. **Download** → Baixa áudio usando pytube
3. **Conversão** → Converte para MP3 com moviepy
4. **Metadados** → Aplica tags ID3 com mutagen
5. **Limpeza** → Remove arquivos temporários

## 🔧 Tecnologias

- **Python 3.13+** - Linguagem principal
- **UV** - Gerenciador de pacotes rápido
- **pytube** - Download do YouTube
- **moviepy** - Conversão de áudio/vídeo
- **mutagen** - Metadados de áudio
- **click** - Interface CLI
- **tqdm** - Barras de progresso
- **ruff** - Formatação e linting

## 📝 Exemplos avançados

### Script personalizado

```python
from src.yt_down.config import Config
from src.yt_down.app import YTDownApp
from src.yt_down.logger import setup_logging

# Configurar logging
logger = setup_logging("INFO")

# Criar configuração personalizada
config = Config()
config.audio_quality = 320
config.output_format = "mp3"

# Criar aplicação
app = YTDownApp(config)

# Processar vídeo
success = app.process_single_video("https://youtu.be/dQw4w9WgXcQ")
print(f"Sucesso: {success}")
```

### Processamento em lote

```python
urls = [
    "https://youtu.be/video1",
    "https://youtu.be/video2", 
    "https://youtu.be/video3"
]

successful, total = app.process_multiple_urls(urls)
print(f"Processados: {successful}/{total}")
```

## 🐛 Troubleshooting

### Problemas comuns

**Erro de importação do pytube:**

```bash
uv sync  # Reinstalar dependências
```

**Erro de permissão:**

```bash
chmod +x main.py
```

**Vídeo indisponível:**

- Verifique se o vídeo é público
- Tente novamente mais tarde
- Use modo verbose para mais detalhes

**Qualidade baixa:**

- Aumente o valor de `--quality`
- Alguns vídeos têm limitações de qualidade

## 📄 Licença

Este projeto está sob a licença MIT. Veja [LICENSE](LICENSE) para detalhes.

## ⚠️ Aviso Legal

Esta ferramenta é destinada apenas para uso educacional e download de conteúdo próprio ou com permissão. Respeite os direitos autorais e os termos de serviço do YouTube.

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

---

### Desenvolvido com ❤️ e Python
