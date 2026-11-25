"""Create a two-cell Tiled atlas before and after repacking. Python 3, stdlib only.

Run: python two_tile_example.py
Open the three .tsj files in the new atlas-ferry-two-tile directory using Tiled.
You may reuse these example files in personal and commercial game projects.
"""

import json
import struct
import zlib
from pathlib import Path

SIZE = 8
OUTPUT = Path("atlas-ferry-two-tile")


def png_chunk(tag, body):
    return (struct.pack(">I", len(body)) + tag + body
            + struct.pack(">I", zlib.crc32(tag + body)))


def write_sheet(name, order):
    raw = bytearray()
    for y in range(SIZE):
        raw.append(0)
        for tile in order:
            for x in range(SIZE):
                color = (227, 162, 72) if tile == "lamp" else (57, 118, 114)
                if (tile == "lamp" and x == 3) or (tile == "wall" and y == 3):
                    color = (248, 244, 219)
                raw.extend(color)
    header = struct.pack(">IIBBBBB", SIZE * 2, SIZE, 8, 2, 0, 0, 0)
    data = b"\x89PNG\r\n\x1a\n" + png_chunk(b"IHDR", header)
    data += png_chunk(b"IDAT", zlib.compress(raw)) + png_chunk(b"IEND", b"")
    (OUTPUT / name).write_bytes(data)


def tileset(image, tiles):
    return dict(type="tileset", version="1.10", tiledversion="1.12.2",
                name=image[:-4], tilewidth=SIZE, tileheight=SIZE,
                columns=2, tilecount=2, margin=0, spacing=0, image=image,
                imagewidth=SIZE * 2, imageheight=SIZE, tiles=tiles)


def annotations(wall, lamp):
    shape = dict(id=1, name="ledge", type="", x=0, y=4, width=8, height=4,
                 rotation=0, visible=True)
    return [
        dict(id=wall, objectgroup=dict(type="objectgroup", draworder="index",
                                       objects=[shape])),
        dict(id=lamp, animation=[dict(tileid=lamp, duration=220),
                                 dict(tileid=wall, duration=140)])
    ]


def main():
    OUTPUT.mkdir(exist_ok=False)
    write_sheet("old.png", ["wall", "lamp"])
    write_sheet("new.png", ["lamp", "wall"])
    cases = {"old": tileset("old.png", annotations(0, 1)),
             "new": tileset("new.png", []),
             "expected": tileset("new.png", annotations(1, 0))}
    for name, value in cases.items():
        (OUTPUT / (name + ".tsj")).write_text(
            json.dumps(value, indent=2) + "\n", encoding="utf-8")
    print("Open old.tsj, new.tsj and expected.tsj in", OUTPUT.resolve())


if __name__ == "__main__":
    main()
