# tkinter-standalone

This is the tkinter package, copied from the python 3.13 source tree for building
in a flatpak package without having to recompile and distribute all of Python, as
this leads to other compatibility problems.

Sources:
 - https://github.com/python/cpython/tree/3.13/Lib/tkinter
 - https://github.com/python/cpython/blob/3.13/Modules/_tkinter.c

## Add to flatpak with:

```json
{
  "name": "tkinter",
  "buildsystem": "simple",
  "build-commands": [
    "pip3 install --prefix=${FLATPAK_DEST} --no-build-isolation ."
  ],
  "sources": [
    {
      "type": "git",
      "url": "https://github.com/iwalton3/tkinter-standalone",
      "commit": "d9cb97c5bd4f814c73678366e0e48220776b6ad3"
    }
  ],
  "modules": [
    {
      "name": "tcl9.0",
      "sources": [
        {
          "type": "archive",
          "url": "https://prdownloads.sourceforge.net/tcl/tcl9.0.2-src.tar.gz",
          "sha256": "e074c6a8d9ba2cddf914ba97b6677a552d7a52a3ca102924389a05ccb249b520",
          "config-opts": ["--disable-zipfs"],
          "x-checker-data": {
              "type": "html",
              "url": "https://sourceforge.net/projects/tcl/rss",
              "pattern": "<link>(https://sourceforge.net/.+/tcl(8\\.6\\.[\\d\\.]*\\d)-src.tar.gz)/download"
          }
        }
      ],
      "subdir": "unix",
      "post-install": [
        "chmod +w ${FLATPAK_DEST}/lib/libtcl9.0.so"
      ]
    },
    {
      "name": "tk9.0",
      "sources": [
        {
          "type": "archive",
          "url": "https://prdownloads.sourceforge.net/tcl/tk9.0.2-src.tar.gz",
          "sha256": "76fb852b2f167592fe8b41aa6549ce4e486dbf3b259a269646600e3894517c76",
          "config-opts": ["--disable-zipfs"],
          "x-checker-data": {
              "type": "html",
              "url": "https://sourceforge.net/projects/tcl/rss",
              "pattern": "<link>(https://sourceforge.net/.+/tk(8\\.6\\.[\\d\\.]*\\d)-src.tar.gz)/download"
          }
        }
      ],
      "subdir": "unix",
      "post-install": [
        "chmod +w ${FLATPAK_DEST}/lib/libtcl9tk9.0.so"
      ]
    }
  ]
}
```

Based on: https://github.com/RomanKharin/flatpak-it-all
