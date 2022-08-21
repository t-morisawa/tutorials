```
brew install libusb
brew install lsusb
pip install nfcpy
```

メモ: Macだと動かなかった.

```
% python main.py
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    clf = nfc.ContactlessFrontend('usb')
  File "/Users/taumu/.pyenv/versions/3.8.2/lib/python3.8/site-packages/nfc/clf/__init__.py", line 76, in __init__
    raise IOError(errno.ENODEV, os.strerror(errno.ENODEV))
OSError: [Errno 19] Operation not supported by device
```
