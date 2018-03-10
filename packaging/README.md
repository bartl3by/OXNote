# OXNote Packaging

## MacOS

### Requirements
* Python 3.6
* Python Modules:
    * pyinstaller
* System Modules:
    * UPX

### Module Installation
##### Preparation for building and signing the OSX packages:
```
brew install upx
pip3 install pyinstaller
```

### Packaging

##### Create spec file for package building:
```
pyinstaller -n OXNote --windowed --osx-bundle-identifier=de.bartl3by.OXNote --icon=resources/designs/default/OXNoteTray.icns --add-data resources:resources --distpath tmp/dist --workpath tmp/build oxnote/oxnote.py
```
##### Build a package:
```
pyinstaller --windowed --distpath tmp/dist --workpath tmp/build packaging/macos/OXNote.spec
```
##### Sign a package:

[Follow pyinstallers guide for creating a self signed certificate](https://github.com/pyinstaller/pyinstaller/wiki/Recipe-OSX-Code-Signing), [Or check the Apple OpenSSL description](https://developer.apple.com/library/content/technotes/tn2206/_index.html#//apple_ref/doc/uid/DTS40007919-CH1-TNTAG10). First, unlock the key chain:
```
security show-keychain-info ~/Library/Keychains/login.keychain
```
Or alternatively try this if the command above won't show the password requests for the keychain):
```
security set-key-partition-list -S apple-tool:,apple: -s -k`pwd` ~/Library/Keychains/login.keychain
```
Next, find the identity string for the custom certificate you created (It is the 42 character starting value of each line):
```
security find-identity -v
```
Then, sign the package you created earlier:
```
codesign --deep --force --sign "{IDENTITY}" --timestamp=none OXNote.app
```
Optionally, verify that the packages have been signed successfully by using some or all of the following tools:
```
spctl --verbose --assess --type execute -v OXNote.app
```
```
spctl --raw --assess --type execute -v OXNote.app
```
```
spctl --assess --verbose=4 OXNote.app
```
