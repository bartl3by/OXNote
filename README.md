# OXNote

## Table of contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Author](#author)
- [License](#license)

## <a name="overview"></a>Overview
OXNote is a desktop application for Open-Xchange AppSuite users designed for taking, organizing and sharing richtext notes. Notes created with OXNote will be stored on a remote Open-Xchange AppSuite account by using the OX Drive synchronization interface and are therefore accessible on all clients OXNote has been installed to.

### Screenshots

![OXNote Screenshot](resources/screenshots/oxnote_screenshot_1.png?raw=true "OXNote Screenshot")

![OXNote Screenshot](resources/screenshots/oxnote_screenshot_2.png?raw=true "OXNote Screenshot")

![OXNote Screenshot](resources/screenshots/oxnote_screenshot_3.png?raw=true "OXNote Screenshot")

## <a name="installation"></a>Installation

### Prerequisites
* MacOS > 10.12
* Python 3.6

### Python Module Dependencies
* pyqt5
* requests
* urllib3
* simplejson
* keyring
* qtpy
* wheel
* ruamel.yaml
* python-slugify

### Installing Python Module Dependencies
In order to be able to start OXNote on MacOS, install the required python libraries:
```
pip3 install -r requirements.txt
```
The QtAwesome python module is required for the Font Awesome icon set, due to a bug that has not yet been fixed in the pypi repository packages it is recommended to install the latest QtAwesome version from github.com/spyder-ide/qtawesome:
```
git clone https://github.com/spyder-ide/qtawesome
python3 setup.py bdist_wheel
pip3 install dist/QtAwesome-0.5.0.dev0-py2.py3-none-any.whl 
```

## <a name="usage"></a>Usage
```
python3 oxnote/oxnote.py
```

## <a name="troubleshooting"></a>Troubleshooting
* Make sure that you are using Python 3.6
* Make sure that module dependencies were satisfied in the correct Python environment
* By default log files will be written to .oxnote/logs, adjust the desired loglevel in configuration/logging.yaml

## <a name="author"></a>Author
Benjamin Otterbach ([@bartl3by](https://github.com/bartl3by))

## <a name="license"></a>License
This project is licensed under GNU General Public License (GPL) v3, see the [LICENSE](LICENSE) file for details.
