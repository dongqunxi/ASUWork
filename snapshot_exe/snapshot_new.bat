set mesh=%1
set pic=%2
set viewpoint=%3
G3dOGL -st %viewpoint% -geom 600x600+0+0 -background white -sharpedgecolor 4288020480 -thickb 3 -thicks 3 -thickn 0 -key DeDb -lighta 0.5 -lights 0.75 -imagen %pic%.jpg -dbuffer 0 -picture %mesh%.m