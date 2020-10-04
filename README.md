# PyEnigma
<img src="/img/enigma_icon.jpg" width="150" height="150">
Enigma machine emulator written in python 3.8

### -------- API ---------
CLASS : "pyenigma"  

  - init(a, b, c)           : initialises the machine. a,b,c are positions of rotors which serve as **key**.
  - currentSetting()        : returns list of initial positions of rotors.
  - changeSetting(a, b, c)  : initialises the machine, with new rotor positions.
  - resetZ()                : resets to 0,0,0 setting.
  - reset()                 : reset to last used setting.
  - run(msg)                : encrypts/decrypts message "msg".
