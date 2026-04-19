# pymadcad Examples

Scripts para abrir exemplos do pymadcad.

## Uso

```bash
# Rodar exemplo do rolamento (bearing)
./examples/run_bearing.sh

# Rodar exemplo de porca (nut)
./examples/run_nut.sh
```

## Exemplos Disponíveis

| Script | Exemplo |
|--------|--------|
| `run_bearing.sh` | Rolamento com esferas |
| `run_nut.sh` | Porca padrão |

## Requisitos

```bash
pip install pymadcad==0.19.1
pip install processional
pip install uimadcad
```

Exportar:
```bash
export LIBGL_ALWAYS_SOFTWARE=1
```