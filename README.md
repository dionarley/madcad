# MadCAD Setup - Problemas Conhecidos

## Problema: brick() gera coordenadas NaN

### Sintoma

```python
from madcad import *
b = brick()
print(b.points)
# Output: [dvec3(-nan, -nan, -nan), ...]
```

### Causa Raiz

A função `brick()` usa `Box` com valores padrão:
- `center=vec3(0)` 
- `width=vec3(-inf)` (infinito negativo)

Ao calcular `box.min = center - width/2`:
- `-inf/2 = inf` (infinito positivo)
- `box.min = vec3(0,0,0) - vec3(inf)` = `inf`
- `box.max = vec3(0,0,0) + vec3(inf)` = `inf`

Mas a matemática `inf - inf = nan` (indeterminação):
- `box.center = (min + max)/2 = (inf + (-inf))/2 = nan`

Isso propaga para todas as coordenadas do mesh.

### Solução

Use parâmetros explícitos:

```python
from madcad import *

# Errado - gera NaN:
b = brick()

# Correto - fornece center e width finitos:
b = brick(center=vec3(0,0,0), width=vec3(1,1,1))
show([b])

# Ou use dimensões específicas:
b = brick(min=vec3(-0.5,-0.5,-0.5), max=vec3(0.5,0.5,0.5))
```

### Outros Exemplos Afetados

Qualquer função que usa valores默认值 com `-inf`:
- `square()` pode ter problema similar
- `parallelogram()` com default infin

Sempre use parâmetros explícitos para safety.

---

## Ambiente de Teste

- **OS**: Arch Linux
- **Python**: 3.12 ou 3.14
- **pymadcad**: 1.0.1 (latest)
- **Display**: DISPLAY=:1

### Teste Rápido

```bash
# Com display
source venv/bin/activate
python -c "from madcad import *; b=brick(center=vec3(0,0,0), width=vec3(1,1,1)); show([b])"

# Headless (sem monitor)
xvfb-run -a python -c "from madcad import *; b=brick(center=vec3(0,0,0), width=vec3(1,1,1)); print('OK')"
```

---

## Instalação

```bash
chmod +x script.sh
./script.sh
```