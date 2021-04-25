from pathlib import Path
from svgpathtools.svg_to_paths import svg2paths
import svgpath2mpl

CUR_DIR = Path(__file__).parent.absolute()
path_to_svg =  CUR_DIR / 'svg_symbols/station_schematics.svg'
print(path_to_svg)

# svg_path = svg_to_paths.svg2paths(path_to_svg)
# station_marker = svgpath2mpl.parse_path(svg_path)
symbols = {'station': 'o'}