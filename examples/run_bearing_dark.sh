#!/bin/bash
# Run pymadcad bearing in dark mode

export LIBGL_ALWAYS_SOFTWARE=1

python3 << 'EOF'
import sys
from PyQt5.QtWidgets import QApplication
from uimadcad import settings

app = QApplication(sys.argv)
settings.use_color_preset('dark-green')
print('Dark-green mode enabled')

from madcad import *
from madcad.rendering import Scene

dint, dext, h = 16, 35, 11
rint, rext = dint/2, dext/2
c, w, e = 0.05*h, 0.5*h, 0.15*(dext-dint)
axis = Axis(O,Z)
interior = Wire([vec3(rint+e, 0, w), vec3(rint, 0, w), vec3(rint, 0, -w), vec3(rint+e, 0, -w)]).segmented().flip()
exterior = Wire([vec3(rext-e, 0, -w), vec3(rext, 0, -w), vec3(rext, 0, w), vec3(rext-e, 0, w)]).segmented().flip()
part = revolution(web([exterior, interior]), axis, 4)
part.mergeclose()

# Use show which starts Qt event loop
show([part])
print('Bearing displayed in dark-green mode')
EOF