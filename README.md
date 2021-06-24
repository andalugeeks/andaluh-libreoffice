# andaluh-libreoffice

An extension for LibreOffice Writer to help you transliterating español (spanish) spelling to andaluz proposals. 

This extension has been developed with [Python-UNO bridge](http://www.openoffice.org/udk/python/python-bridge.html) and [andaluh-py](https://github.com/andalugeeks/andaluh-py) library embedded on the extension itself. No need to download any dependencies.

<a href="https://github.com/andalugeeks/andaluh-libreoffice/blob/master/img/test.jpg?raw=true"><img width="800" alt="andaluh-libreoffice about" src="https://github.com/andalugeeks/andaluh-libreoffice/blob/master/img/test.jpg?raw=true"></a>

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Roadmap](#roadmap)
- [Support](#support)
- [Contributing](#contributing)

## Description

The **Andalusian varieties of [Spanish]** (Spanish: *andaluz*; Andalusian) are spoken in Andalusia, Ceuta, Melilla, and Gibraltar. They include perhaps the most distinct of the southern variants of peninsular Spanish, differing in many respects from northern varieties, and also from Standard Spanish. Further info: https://en.wikipedia.org/wiki/Andalusian_Spanish.

This package introduces transliteration functions to convert *español* (spanish) spelling to andaluz. As there's no official or standard andaluz spelling, andaluh-js is adopting the **EPA proposal (Estándar Pal Andaluz)**. Further info: https://andaluhepa.wordpress.com. Other andaluz spelling proposals are planned to be added as well.

## Installation

You'll find an installation file at `dist/AndaluhLibreOffice-0.1.0.oxt`. It has been tested under Linux Ubuntu 20.04 and Windows 10 with LibreOffice 7.x

## Usage

Upon extension installation you'll see new toolbard icon named `Andaluh`. Also under `Tools -> AndaluhLibre`.

## Development

Use `python3`. Clone this repo, then: 

* Do your changes editing files under `src/`.
* Install `andaluh-py` under `src/AndaluhLibre/pythonpath`
* Zip them and rename the zip file as `.oxt`.

Get inspiration with the `build.sh` script (for Linux):

```
# Install/Upgrade andaluh dependency from pip
pip3 install andaluh -t src/AndaluhLibre/pythonpath --upgrade

# Package as oxt libreoffice extension file
mkdir -p dist
cd src

# If extension was installed, remove first
unopkg remove es.andaluh.AndaluhLibre
rm -f ../dist/AndaluhLibreOffice-0.1.0.oxt
zip -r ../dist/AndaluhLibreOffice-0.1.0.oxt *
unopkg add -f "../dist/AndaluhLibreOffice-0.1.0.oxt"
soffice --norestore
```

## Roadmap

* Add andalusian dictionary for grammar corrections.
* Add LibreOffice Calc formulas to translate to andaluh as well.

## Support

Please [open an issue](https://github.com/andalugeeks/andaluh-libreoffice/issues/new) for support.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and open a pull request.
