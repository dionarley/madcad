# Problemas e Soluções

## Problema 1: brick() gera NaN

**Sintoma:** `brick()` sem parâmetros gera coordenadas NaN.

**Causa:** width=-inf causa inf-inf=nan no cálculo de Box.

**Solução:** Usar parâmetros explícitos:
```python
b = brick(center=vec3(0,0,0), width=vec3(1,1,1))
```

---

## Problema 2: GLSL 4.30 não suportado

**Sintoma:** `GLSL 4.30 is not supported`

**Causa:** GPU não suporta OpenGL 4.30.

**Solução:**
```bash
export LIBGL_ALWAYS_SOFTWARE=1
```

---

## Problema 3: note_* não definidas

**Sintoma:** `NameError: name 'note_radius' is not defined`

**Causa:** Funções existem em `madcad.scheme` mas não são exportadas.

**Solução (precisa correção no código):**
```python
# Precisa adicionar em madcad/__init__.py
from madcad.scheme import note_radius, note_leading, note_distance
```

---

## Problema 4: ImportError ivec4

**Sintoma:** `ImportError: cannot import name 'ivec4'`

**Causa:** Incompatibilidade uimadcad vs pymadcad>=1.0

**Solução:**
```bash
pip install "pymadcad==0.19.1"
```

---

## Problema 5: Ícone não abre

**Sintoma:** Clica no ícone e nada acontece.

**Solução:** Editar `/usr/share/applications/madcad.desktop`:
```ini
Exec=bash -c "export LIBGL_ALWAYS_SOFTWARE=1; python3 -m uimadcad"
```