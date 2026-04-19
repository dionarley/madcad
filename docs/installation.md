# Instalação

## Dependências do Sistema (Arch Linux)

```bash
sudo pacman -S python-pip python-virtualenv \
    libglvnd opencl-header mesa glfw \
    qt5-base qt5-x11extras
```

## Python

```bash
# Versão recomendada: Python 3.12 ou 3.14
python --version
```

## pymadcad

```bash
pip install pymadcad==0.19.1
```

## uimadcad

```bash
pip install uimadcad
pip install processional
```

## Verificar Instalação

```bash
python -c "from madcad import *; print('OK')"
```
