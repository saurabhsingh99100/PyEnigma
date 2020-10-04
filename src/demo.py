import PyEnigma as PE

# setting = 4,17,9

m = PE.pyenigma(4,17,9)

print("current setting : "+str(m.currentSetting()))

msg = "THIS IS A PYTHON EMULATION OF AN ENIGMA MACHINE"

print("msg              :"+ msg+"\n")

enc = m.run(msg)
print("encrypted text   :"+ enc)

m.reset()
print("decrypted text   :"+ m.run(enc))


