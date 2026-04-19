# Docker Stack para Desenvolvimento pymadcad

## Visão Geral

Este diretório contém a configuração Docker para desenvolvimento do pymadcad.

## Estrutura

```
madcad/
├── pymadcad/           # Repositório clonado do pymadcad
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── DOCKER.md
├── uimadcad/          # Repositório clonado do uimadcad (GUI)
└── script.sh          # Script de instalação local (não-Docker)
```

## Quick Start

```bash
cd pymadcad

# Build da imagem
docker compose build dev

# Shell interativo
docker compose run --rm dev

# Rodar testes (headless)
docker compose run --rm test-headless
```

## Comandos Úteis

```bash
# Desenvolvimento com display local (Linux)
DISPLAY=$DISPLAY docker compose run --rm dev

# Tests específicos
docker compose run --rm test-headless pytest tests/test_mesh.py -v

# Com GPU NVIDIA
docker compose run --rm --gpus all dev
```

## Notas

- O Dockerfile usa Python 3.12 e Rust (via maturin)
- Xvfb fornece display virtual para testes headless
- Volume é mountado para hot-reload durante desenvolvimento