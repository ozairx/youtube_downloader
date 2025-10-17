# YT-Down - YouTube to MP3 Downloader

Este projeto é uma ferramenta para baixar playlists do YouTube e converter os vídeos para formato MP3.

## Descrição do Projeto

O **yt-down** é uma aplicação Python que permite:

- Baixar vídeos individuais ou playlists completas do YouTube
- Converter automaticamente os vídeos para formato MP3
- Organizar os arquivos baixados em estrutura de pastas
- Aplicar metadados aos arquivos MP3 (título, artista, etc.)

## Tecnologias Utilizadas

- **Python 3.13+**: Linguagem principal
- **UV**: Gerenciador de pacotes e ambiente virtual rápido
- **pytube**: Para download de vídeos do YouTube
- **moviepy**: Para conversão de vídeo para áudio
- **python-dotenv**: Para gerenciamento de variáveis de ambiente
- **ruff**: Para linting e formatação do código
- **click**: Para interface de linha de comando
- **tqdm**: Para barras de progresso
- **mutagen**: Para metadados de arquivos de áudio

## Estrutura do Projeto

```bash
yt-down/
├── main.py              # Arquivo principal da aplicação
├── pyproject.toml       # Configurações do projeto e dependências
├── README.md           # Documentação do projeto
├── .env.example        # Exemplo de variáveis de ambiente
├── downloads/          # Pasta para arquivos baixados (criada automaticamente)
└── .vscode/           # Configurações do VS Code e Copilot
    ├── settings.json   # Configurações do editor
    ├── launch.json     # Configurações de debug
    └── extensions.json # Extensões recomendadas
```

## Instalação

### 🚀 Instalação Rápida (Recomendada)

```bash
# Usando uvx (mais rápido, sem instalação permanente)
uvx yt-down --help

# Ou usando pipx (instalação isolada)
pipx install yt-down
```

### 🔧 Instalação para Desenvolvimento

```bash
# Clone o repositório
git clone https://github.com/ozairx/yt-down.git
cd yt-down

# Instale as dependências com UV
uv sync
```

Para mais opções de instalação, veja o [Guia de Instalação](docs/INSTALL.md).

## Uso

### Baixar um vídeo individual

```bash
uv run python main.py --url "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Baixar uma playlist

```bash
uv run python main.py --playlist "https://www.youtube.com/playlist?list=PLAYLIST_ID"
```

### Opções disponíveis

- `--output-dir`: Diretório de saída (padrão: ./downloads)
- `--quality`: Qualidade do áudio (padrão: 192kbps)
- `--format`: Formato de saída (padrão: mp3)

## Configurações do Copilot

Este projeto inclui configurações otimizadas para o GitHub Copilot:

### Funcionalidades Habilitadas

- **Sugestões inline**: Ativadas para Python
- **Autocompletar inteligente**: Configurado para desenvolvimento de aplicações de mídia
- **Contexto do projeto**: O Copilot entende que este é um projeto de download e conversão de mídia
- **Formatação automática**: Código formatado automaticamente com black e ruff

### Snippets Sugeridos

O Copilot pode ajudar com:

- Implementação de download de vídeos do YouTube
- Conversão de formatos de áudio/vídeo
- Manipulação de metadados de arquivos MP3
- Gerenciamento de arquivos e diretórios
- Tratamento de erros em downloads
- Validação de URLs do YouTube

## Desenvolvimento

### Debug

Use as configurações de debug pré-configuradas no VS Code:

- **Python: Current File**: Executa o arquivo atual
- **Python: Main**: Executa o main.py
- **Python: Download Playlist**: Executa com argumentos de exemplo

### Linting e Formatação

O projeto usa Ruff para linting e formatação automática. Execute:

```bash
uv run ruff check .     # Verificar problemas
uv run ruff format .    # Formatar código
uv run ruff check --fix .  # Corrigir problemas automaticamente
```

## Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Aviso Legal

Este projeto é apenas para fins educacionais. Respeite os termos de serviço do YouTube e os direitos autorais do conteúdo baixado.
