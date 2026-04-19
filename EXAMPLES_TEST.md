# pymadcad Examples Test Results

## Resumo
- **Total**: 17 exemplos
- **OK**: 3 (timeout=2 abre janela)
- **Erro**: 12
- ** Timeout**: 2

## Exemplos OK (abrem janela)
- bearing.py ⏱️
- elliptic-gearbox.py ⏱️
- kinematic-compound-planetary.py ✅
- kinematic-planetary.py ✅
- planetary-gearbox.py ✅

## Erros Identificados

### 1. note_radius / note_leading / note_distance não definidos
Erro: `NameError: name 'note_radius' is not defined`

**Causa**: funções existem em `madcad.scheme` mas não são exportadas no `madcad` main

**Arquivos afetados**: 10 exemplos
- axis-holder.py
- birfield.py
- compound-planetary.py
- differential-asymetric.py
- differential-symetric.py
- double-universal-joint.py
- nut.py
- offscreen.py
- universal-joint.py

**Solução needed**: Importar de `madcad.scheme`:
```python
from madcad.scheme import note_radius, note_leading, note_distance
```

### 2. settings.primitives não existe
Erro: `AttributeError: module 'madcad.settings' has no attribute 'primitives'`

**Arquivo**: elliptic-gearbox-traversing.py

### 3. matchclosest não existe
Erro: `ImportError: cannot import name 'matchclosest' from 'madcad.generation'`

**Arquivo**: screenshots.py

### 4. TriangulationError
Erro: `no more feasible triangles (algorithm failure or bad input outline)`

**Arquivo**: text.py

---

## Log Completo
Ver: examples_test.log