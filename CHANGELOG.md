# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Preparação para distribuição via pipx
- Configuração para empacotamento em repositórios Linux

## [0.1.0] - 2025-10-11

### Added

- Download de vídeos individuais do YouTube
- Download de playlists completas
- Conversão automática para MP3 com qualidade configurável
- Interface CLI com argumentos completos
- Sistema de logging configurável
- Validação de URLs do YouTube
- Metadados ID3 automáticos
- Processamento paralelo configurável
- Tratamento robusto de erros
- Configuração via variáveis de ambiente
- Sanitização de nomes de arquivos
- Barras de progresso para downloads
- Limpeza automática de arquivos temporários

### Technical

- Arquitetura modular com separação de responsabilidades
- Configuração com UV e Ruff
- Suporte a Python 3.9+
- Dependências: pytube, moviepy, click, tqdm, mutagen
- Configurações VS Code para desenvolvimento

[Unreleased]: https://github.com/ozairx/yt-down/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/ozairx/yt-down/releases/tag/v0.1.0
