# tkinter-standalone

This is the tkinter package, copied from the python 3.9 source tree for building
in a flatpak package without having to recompile and distribute all of Python, as
this leads to other compatibility problems.

Sources:
 - https://github.com/python/cpython/tree/3.9/Lib/tkinter
 - https://github.com/python/cpython/blob/3.9/Modules/_tkinter.c

## Add to flatpak with:

```json
{
  "name": "tkinter",
  "buildsystem": "simple",
  "build-commands": [
      "pip3 install --prefix=${FLATPAK_DEST} ."
  ],
  "sources": [
    {
      "type": "git",
      "url": "https://github.com/iwalton3/tkinter-standalone",
      "commit": "2301112d142ebaf7532b25600c77d1a2edc9ef04"
    }
  ],
  "modules": [
    {
      "name": "tcl8.6.8",
      "sources": [
        {
          "type": "archive",
          "url": "http://prdownloads.sourceforge.net/tcl/tcl8.6.6-src.tar.gz",
          "sha256": "a265409781e4b3edcc4ef822533071b34c3dc6790b893963809b9fe221befe07"
        }
      ],
      "subdir": "unix",
      "post-install": [
        "chmod +w /app/lib/libtcl8.6.so"
      ]
    },
    {
      "name": "tk8.6.6",
      "sources": [
        {
          "type": "archive",
          "url": "http://prdownloads.sourceforge.net/tcl/tk8.6.6-src.tar.gz",
          "sha256": "d62c371a71b4744ed830e3c21d27968c31dba74dd2c45f36b9b071e6d88eb19d"
        }
      ],
      "subdir": "unix",
      "post-install": [
        "chmod +w /app/lib/libtk8.6.so"
      ]
    }
  ]
}
```

Based on: https://github.com/RomanKharin/flatpak-it-all
