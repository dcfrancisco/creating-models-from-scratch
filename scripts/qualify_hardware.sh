#!/usr/bin/env bash
set -euo pipefail

uname -a
cat /proc/cpuinfo | grep -E "(model name|flags|cpu MHz)" | head -20
cat /proc/meminfo | head -10
df -h .
python3 --version
python3 -c "import numpy; print('numpy', numpy.__version__); import numpy as np; A=np.random.randn(100,100); B=np.random.randn(100,100); t=__import__('time').time(); C=A@B; print('matmul 100x100:', __import__('time').time()-t, 's')"
python3 -c "import torch; print('torch', torch.__version__); x=torch.randn(3,3, requires_grad=True); print('tensor ok'); y=x.sum(); y.backward(); print('autograd ok')" 2>&1 || echo "torch not available or not compatible"
