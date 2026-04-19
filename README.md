# MadCAD Setup - Problemas e Soluções

## Problema 1: uimadcad não abre (command not found)

### Sintoma
```
$ uimadcad
bash: command not found: uimadcad
```

### Causa
uimadcad não foi instalado ou não está no PATH.

### Solução
```bash
pip install uimadcad
python -m uimadcad  # ou uimadcad se estiver no PATH
```

---

## Problema 2: uimadcad crash com ImportError (ivec4)

### Sintoma
```
ImportError: cannot import name 'ivec4' from 'madcad.mathutils'
```

### Causa
Incompatibilidade entre uimadcad e pymadcad >= 1.0. uimadcad precisa de `pymadcad < 1.0`.

### Solução
```bash
pip install "pymadcad<1.0" --force-reinstall
```

Versão testada: **pymadcad 0.20.1** funciona com uimadcad 0.8.0

---

## Problema 3: brick() gera coordenadas NaN

### Sintoma
```python
from madcad import *
b = brick()
print(b.points)  # [dvec3(-nan, -nan, -nan), ...]
```

### Causa
Valores padrão `-inf` causam `inf - inf = nan` no cálculo de Box.

### Solução
Use parâmetros explícitos:
```python
b = brick(center=vec3(0,0,0), width=vec3(1,1,1))
# ou
b = brick(min=vec3(-0.5,-0.5,-0.5), max=vec3(0.5,0.5,0.5))
```

---

## Instalação Completa (Arch Linux)

```bash
# 1. Dependências do sistema (Arch)
sudo pacman -S python-pip python-virtualenv \
    libglvnd opencl-header mesa glfw \
    qt5-base qt5-x11extras

# 2. Instalar pymadcad versão compatível
pip install "pymadcad<1.0"

# 3. Instalar uimadcad
pip install uimadcad

# 4. Testar
python -c "from madcad import *; print('OK')"
python -m uimadcad
```

---

## Hyprland/Wayland

Para rodar com Hyprland:
```bash
QT_QPA_PLATFORM=wayland python -m uimadcad
```

Software rendering:
```bash
LIBGL_ALWAYS_SOFTWARE=1 python -m uimadcad
```

---

## Docker

```bash
cd pymadcad

# Build
docker compose build dev

# Development
docker compose run --rm dev

# Testes headless
docker compose run --rm test-headless
```

---

## Ambiente de Teste

- **OS**: Arch Linux (hyprland)
- **Python**: 3.14
- **pymadcad**: 0.20.1
- **uimadcad**: 0.8.0

### Teste Rápido

```bash
# Com display
python -c "from madcad import *; b=brick(center=vec3(0,0,0), width=vec3(1,1,1)); show([b])"

# Headless
xvfb-run -a python -c "from madcad import *; b=brick(center=vec3(0,0,0), width=vec3(1,1,1)); print('OK')"
```

---

## Instalação (script.sh)

```bash
chmod +x script.sh
./script.sh
```