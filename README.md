# hydrogen-drumkit-creator
Create drumkit XML for Hydrogen drum machine from drum sample files.

[Hydrogen](http://www.hydrogen-music.org/hcms/) is the best free drum machine. 

# Usage

Generate `drumkit.xml` into the sample path:

```sh
$ python generate_kit.py -p /sample/directory/path/ -e .wav > /sample/directory/path/drumkit.xml
```

Copy kit to your `~/.hydrogen/data/drumkits/`:

```sh
$ cp -r  /sample/directory/path ~/.hydrogen/data/drumkits/
```

Then enjoy making fabulous drum tracks!
