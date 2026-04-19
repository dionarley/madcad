# pymadcad Examples

Scripts para abrir exemplos do pymadcad.

## Uso

```bash
# Launcher interativo
python3 run_example.py

# Ou direto
./examples/run_bearing.sh
```

## Exemplos Testados (funcionando com pymadcad 0.19.1)

| Exemplo | Status |
|---------|--------|
| bearing | ✅ OK |
| kinematic-planetary | ✅ OK |

## Exemplos com Bugs (pymadcad 0.19.1)

| Exemplo | Erro |
|---------|------|
| nut | `note_leading` not defined |
| axis-holder | `note_leading` not defined |
| universal-joint | `note_radius` not defined |
| text | TriangulationError |
| planetary-gearbox | various |

## Requisitos

```bash
pip install pymadcad==0.19.1
pip install processional
pip install uimadcad

export LIBGL_ALWAYS_SOFTWARE=1
```