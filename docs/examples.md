# Exemplos

## Exemplos Testados

**Funcionando:**
- bearing.py ✅
- kinematic-planetary.py ✅
- kinematic-compound-planetary.py ✅
- planetary-gearbox.py ✅

**Com erros (note_* não exportadas):**
- axis-holder.py
- nut.py
- universal-joint.py
- differential-symetric.py
- differential-asymetric.py

**Outros erros:**
- elliptic-gearbox-traversing.py (settings.primitives)
- screenshots.py (matchclosest)
- text.py (TriangulationError)

## Rodar Exemplos

### Via UI (recomendado)
```bash
python -m uimadcad
# File > Open > exemplo.py
```

### Via CLI
```bash
./run_example_cli.sh pymadcad/examples/bearing.py
```

### Com Dark Mode
```bash
./run_example_cli.sh pymadcad/examples/bearing.py dark-green
```