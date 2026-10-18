"""Make the dotted world map used by the network visualisation.

Land outlines: Natural Earth 1:110m land (public domain), e.g.
https://raw.githubusercontent.com/nvkelso/natural-earth-vector/v5.1.2/geojson/ne_110m_land.geojson

    python3 tools/make_land_dots.py ne_110m_land.geojson

writes _includes/network-land.svg: one SVG path of dots on a regular grid, in the
Equal Earth projection (the same projection, and the same constants, as the
JavaScript in _includes/network.html, which places the nodes).
Requires numpy and matplotlib.
"""
import json
import sys

import numpy as np
from matplotlib.path import Path

A1, A2, A3, A4 = 1.340264, -0.081106, 0.000893, 0.003796
M = np.sqrt(3) / 2
SCALE = 200            # projection units -> SVG units
LAT_MIN = -58          # leave out Antarctica
STEP = 6.5             # dot spacing, SVG units


def forward(lon, lat):
    lam, phi = np.radians(lon), np.radians(lat)
    t = np.arcsin(M * np.sin(phi))
    t2 = t * t
    t6 = t2 * t2 * t2
    x = lam * np.cos(t) / (M * (A1 + 3 * A2 * t2 + t6 * (7 * A3 + 9 * A4 * t2)))
    y = t * (A1 + A2 * t2 + t6 * (A3 + A4 * t2))
    return x * SCALE, -y * SCALE


def inverse(x, y):
    x, y = x / SCALE, -y / SCALE
    t = y.copy()
    for _ in range(12):                                  # Newton on theta
        t2 = t * t
        t6 = t2 * t2 * t2
        f = t * (A1 + A2 * t2 + t6 * (A3 + A4 * t2)) - y
        fp = A1 + 3 * A2 * t2 + t6 * (7 * A3 + 9 * A4 * t2)
        t = t - f / fp
    t2 = t * t
    t6 = t2 * t2 * t2
    lam = M * x * (A1 + 3 * A2 * t2 + t6 * (7 * A3 + 9 * A4 * t2)) / np.cos(t)
    phi = np.arcsin(np.sin(t) / M)
    return np.degrees(lam), np.degrees(phi)


def main(path):
    rings = []
    for feat in json.load(open(path))["features"]:
        g = feat["geometry"]
        polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
        rings += [Path(np.asarray(p[0])) for p in polys]
    x0, _ = forward(-180, 0)
    _, y0 = forward(0, 83.6)
    _, y1 = forward(0, LAT_MIN)
    xs = np.arange(x0, -x0, STEP)
    ys = np.arange(y0, y1, STEP * np.sqrt(3) / 2)
    dots = []
    for i, yy in enumerate(ys):                          # hexagonal grid
        row = xs + (STEP / 2 if i % 2 else 0)
        lon, lat = inverse(row, np.full_like(row, yy))
        ok = (np.abs(lon) <= 180) & (lat >= LAT_MIN)
        pts = np.c_[lon, lat]
        land = np.zeros(len(row), bool)
        for r in rings:
            land |= r.contains_points(pts)
        dots += [(a, yy) for a in row[ok & land]]
    d = "".join(f"M{a:.1f} {b:.1f}h0" for a, b in dots)
    w, h = -2 * x0, y1 - y0
    with open("_includes/network-land.svg", "w") as fh:
        fh.write(f'<path class="land" d="{d}"/>\n')
    print(f"{len(dots)} dots; viewBox {x0:.1f} {y0:.1f} {w:.1f} {h:.1f}")


if __name__ == "__main__":
    main(sys.argv[1])
