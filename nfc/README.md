```
brew install libusb
brew install lsusb
pip install nfcpy
```

メモ: Macだと動かなかった. 使っている機器が認識できていないかもしれない.

```
% python main.py
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    clf = nfc.ContactlessFrontend('usb')
  File "/Users/taumu/.pyenv/versions/3.8.2/lib/python3.8/site-packages/nfc/clf/__init__.py", line 76, in __init__
    raise IOError(errno.ENODEV, os.strerror(errno.ENODEV))
OSError: [Errno 19] Operation not supported by device

% python -m nfc --search-tty
This is the 1.0.4 version of nfcpy run in Python 3.8.2
on macOS-10.16-x86_64-i386-64bit
I'm now searching your system for contactless devices
Traceback (most recent call last):
  File "/Users/taumu/.pyenv/versions/3.8.2/lib/python3.8/runpy.py", line 193, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/Users/taumu/.pyenv/versions/3.8.2/lib/python3.8/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/Users/taumu/.pyenv/versions/3.8.2/lib/python3.8/site-packages/nfc/__main__.py", line 214, in <module>
    main(parser.parse_args())
  File "/Users/taumu/.pyenv/versions/3.8.2/lib/python3.8/site-packages/nfc/__main__.py", line 71, in main
    for dev in nfc.clf.transport.TTY.find("tty")[0]:
TypeError: 'NoneType' object is not subscriptable
```
