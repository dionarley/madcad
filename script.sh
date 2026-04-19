#!/usr/bin/env bash
set -e
set -u

echo "[+] Atualizando sistema..."
sudo apt update

echo "[+] Instalando dependências..."
sudo apt install -y \
    python3 python3-venv python3-dev python3-pip \
    build-essential \
    libgl1-mesa-dev libegl1-mesa-dev \
    libx11-dev libxcursor-dev libxrandr-dev libxi-dev libxxf86vm-dev \
    libglfw3-dev

echo "[+] Criando ambiente virtual..."
python3 -m venv venv
source venv/bin/activate

echo "[+] Atualizando pip..."
pip install --upgrade pip setuptools wheel

# Install pymadcad with a version compatible with your numpy
pip install pymadcad

# FIX: brick() bug workaround - explicitly provide center and width
#
# BUG CONHECIDO: brick() sem parâmetros gera NaN por causa de inf-inf na Box
# Solução: Use parâmetros explícitos center= e width=
#
# Incorrecto (gera NaN):
#   from madcad import *
#   show([brick()])
#
# Correto:
#   from madcad import *
#   b = brick(center=vec3(0,0,0), width=vec3(1,1,1))
#   show([b])

echo "[+] Testando instalação..."
python - <<EOF
from madcad import *

# Workaround para bug do brick() - use parâmetros explícitos
b = brick(center=vec3(0,0,0), width=vec3(1,1,1))
print(f"brick() OK: {len(b.points)} vértices, primeiro ponto: {b.points[0]}")
EOF

echo "[+] Concluído!"