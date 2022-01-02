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
      "commit": "d9cb97c5bd4f814c73678366e0e48220776b6ad3"
    }
  ],
  "modules": [
    {
      "name": "tcl8.6",
      "sources": [
        {
          "type": "archive",
          "url": "https://prdownloads.sourceforge.net/tcl/tcl8.6.12-src.tar.gz",
          "sha256": "26c995dd0f167e48b11961d891ee555f680c175f7173ff8cb829f4ebcde4c1a6"
        }
      ],
      "subdir": "unix",
      "post-install": [
        "chmod +w ${FLATPAK_DEST}/lib/libtcl8.6.so"
      ]
    },
    {
      "name": "tk8.6",
      "sources": [
        {
          "type": "archive",
          "url": "https://prdownloads.sourceforge.net/tcl/tcl8.6.12-src.tar.gz",
          "sha256": "26c995dd0f167e48b11961d891ee555f680c175f7173ff8cb829f4ebcde4c1a6"
        }
      ],
      "subdir": "unix",
      "post-install": [
        "chmod +w ${FLATPAK_DEST}/lib/libtk8.6.so"
      ]
    }
  ]
}
```

Based on: https://github.com/RomanKharin/flatpak-it-all
