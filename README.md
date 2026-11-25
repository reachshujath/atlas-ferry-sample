# Atlas Ferry · Tiled tileset examples

When an artist swaps two cells in a sprite sheet, Tiled still uses the original local tile IDs. A collision shape can move onto a lamp, and an animation can play the wrong frames. This free example lets you inspect the three files side by side.

## Run the example

Download [two_tile_example.py](two_tile_example.py) and run it with Python 3 in a directory where you can create files. It uses the Python standard library.

```sh
python two_tile_example.py
```

The script creates a new directory named `atlas-ferry-two-tile`. Open the following external tilesets in Tiled, leaving both PNGs beside them.

| File | What to inspect |
| --- | --- |
| `old.tsj` | The wall is tile 0 and has a collision rectangle. Tile 1 owns an animation whose frames are 1 and 0. |
| `new.tsj` | The artist swapped the wall and lamp in `new.png`. The destination starts with no annotations. |
| `expected.tsj` | The wall at tile 1 has the rectangle. The lamp at tile 0 plays frame 0 for 220 ms, then frame 1 for 140 ms. |

Atlas Ferry is an offline browser utility for transferring metadata between compatible external Tiled tilesets. Its paid listing is in preparation. This repository contains a free worked example. If you face this problem in your own game, the [issue tracker](https://github.com/reachshujath/atlas-ferry-sample/issues) is open for a short description of the file format and what you had to rebuild. Please use a synthetic example if you include files.

You may use and adapt the fixture generator and its outputs for personal and commercial game development, testing and teaching. AI assisted with the code and documentation. This project is independent of Tiled.
