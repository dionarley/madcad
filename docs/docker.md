# Docker

## Quick Start

```bash
cd pymadcad
docker compose build dev
docker compose run --rm dev
```

## Serviços

| Serviço | Descrição |
|---------|-----------|
| dev | Ambiente de desenvolvimento |
| test-headless | Testes com Xvfb |

## Testes

```bash
docker compose run --rm test-headless pytest tests/
```

## Build

```bash
docker compose build dev
docker compose build --build-arg Maturin_FEATURE_FLAGS=--release dev
```