from definitions import ROOT_DIR
from svgpathtools import svg_to_paths
import svgpath2mpl

path_to_svg = ROOT_DIR / 'utils/topo/symbols/station_schematics.svg'
print(path_to_svg)
svg_path = svg_to_paths.svg2paths(path_to_svg)
station_marker = svgpath2mpl.parse_path(svg_path)
symbols = {'station': station_marker}