# Configuração do Copilot para o projeto yt-down

Este arquivo documenta as configurações específicas do GitHub Copilot para o projeto de download do YouTube.

## Contexto do Projeto

O GitHub Copilot foi configurado para entender que este é um projeto Python que:

- Baixa vídeos e playlists do YouTube
- Converte vídeos para formato MP3
- Manipula arquivos de mídia e metadados
- Usa as bibliotecas pytube, moviepy e python-dotenv

## Configurações Aplicadas

### VS Code Settings (.vscode/settings.json)

- Copilot habilitado para Python e Markdown
- Formatação automática com black
- Linting com ruff
- Organização automática de imports
- Exclusão de pastas de download e cache

### Sugestões Otimizadas

O Copilot pode fornecer sugestões específicas para:

1. **Download de YouTube**: Implementação com pytube
2. **Conversão de Áudio**: Uso do moviepy para MP3
3. **Gerenciamento de Arquivos**: Organização e metadados
4. **Tratamento de Erros**: Para downloads e conversões
5. **CLI Arguments**: Para interface de linha de comando
6. **Logging**: Para monitoramento de processos

### Snippets Comuns

O Copilot reconhece padrões para:

- Validação de URLs do YouTube
- Download de vídeos individuais
- Processamento de playlists
- Conversão de formatos
- Aplicação de metadados ID3

## Uso Recomendado

Para obter as melhores sugestões do Copilot:

1. Use comentários descritivos sobre a funcionalidade
2. Nomeie variáveis e funções de forma clara
3. Mantenha o contexto do projeto em mente
4. Aproveite os snippets pré-configurados
