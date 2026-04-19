# MadCAD Setup - Problemas e Soluções (Arch Linux + Hyprland)

## Problema 0: Ícone não abre (Arch Linux/hyprland)

### Sintoma
- Clica no ícone e nada acontece
- Ou erro: `ModuleNotFoundError: No module named 'madcad'`

### Causa
1. `/usr/bin/madcad` usa Python sistema que não tem pymadcad
2. GPU não suporta OpenGL 4.30 → precisa software rendering

### Solução

Editar `/usr/share/applications/madcad.desktop`:
```ini
Exec=bash -c "export LIBGL_ALWAYS_SOFTWARE=1; /home/dnly/.local/share/mise/installs/python/3.14.2/bin/python3 -m uimadcad"
```

(O caminho do Python pode variar: use `which python3` para verificar)

---

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

### Solução (Arch Linux)
```bash
pip install "pymadcad==0.19.1" --force-reinstall
pip install processional
pip install uimadcad
```

Versão testada: **pymadcad 0.19.1** funciona com uimadcad 0.8.0

Também precisa de:
```bash
pip install processional
```

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

### Problema 4: GLSL 4.30 not supported / uimadcad não abre

### Sintoma
```
_moderngl.Error: GLSL 4.30 is not supported
# ou a janela abre mas fica travada
```

### Causa
Placa de vídeo não suporta OpenGL 4.30 (só suporta até 3.30).

### Solução (FUNCIONA)
```bash
# Software rendering (OBRIGATÓRIO no seu sistema)
export LIBGL_ALWAYS_SOFTWARE=1
python -m uimadcad
```

Para facilitar, adicione no seu ~/.bashrc:
```bash
echo 'export LIBGL_ALWAYS_SOFTWARE=1' >> ~/.bashrc
```

Verificar suporte OpenGL:
```bash
glxinfo | grep "OpenGL version"
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

## Problema 5: Exemplos não funcionan (note_* funções faltando)

### Sintoma
```
NameError: name 'note_radius' is not defined
NameError: name 'note_leading' is not defined
NameError: name 'note_distance' is not defined
```

### Causa
Funções existem em `madcad.scheme` mas não são exportadas no `madcad.__init__`.

### Solução needed
Adicionar ao `madcad/__init__.py`:
```python
from madcad.scheme import note_radius, note_leading, note_distance
```

### Exemplos Testados

**OK (abrem janela):**
- bearing.py, elliptic-gearbox.py
- kinematic-compound-planetary.py, kinematic-planetary.py, planetary-gearbox.py

**Com erros (12):**
- axis-holder.py, birfield.py, compound-planetary.py
- differential-asymetric.py, differential-symetric.py, double-universal-joint.py
- nut.py, offscreen.py, universal-joint.py
- elliptic-gearbox-traversing.py (settings.primitives)
- screenshots.py (matchclosest)
- text.py (TriangulationError)

---

## Teste de Exemplos
Alguns exemplos não executam:

```
NameError: name 'note_leading' is not defined
NameError: name 'note_radius' is not defined
TriangulationError: no more feasible triangles
```

### Exemplos Testados

**Funcionando (pymadcad 0.19.1):**
| Exemplo | Status |
|--------|--------|
| bearing | ✅ OK |
| kinematic-planetary | ✅ OK |

**Com bugs:**
| Exemplo | Erro |
|--------|------|
| nut | `note_leading` not defined |
| axis-holder | `note_leading` not defined |
| universal-joint | `note_radius` not defined |
| text | TriangulationError |
| planetary-gearbox | various |

### Solução
Usar launcher com exemplos funcionais:
```bash
python3 run_example.py
```

---

## Ambiente de Teste

- **OS**: Arch Linux (hyprland)
- **Python**: 3.14
- **pymadcad**: 0.19.1 (compatível com uimadcad)
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