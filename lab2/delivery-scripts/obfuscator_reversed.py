# uncompyle6 version 3.9.2
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.10.11 (v3.10.11:7d4cc5aa85, Apr  4 2023, 19:05:19) [Clang 13.0.0 (clang-1300.0.29.30)]
# Embedded file name: .\obfuscator.py
# Compiled at: 2023-09-30 10:58:34
# Size of source mod 2**32: 633 bytes

#    seed is TheBiteOf87
firstSeed = "TheBiteOf87"
import zipfile
import hashlib, sys
SEED_PATH = "seed.txt"
def findZipPassword():
    with open(SEED_PATH, "r") as f:
        line = f.readline()
    if len(line.split("\t")) == 2:
        n = int(line.split("\t")[0])
        seed = line.split("\t")[1].strip()
        if n == 0:
            print("For the first run, please just place your password in the " + SEED_PATH + " file.")
            exit(1)
    else:
        n = 0
        seed = line.strip()
    pw = hashlib.sha256(str(seed + str(sys.argv[1])).encode("utf-8"))
    #print(pw.hexdigest())
    next_seed = hashlib.sha256(str(seed).encode("utf-8"))
    with open(SEED_PATH, "w") as f:
        f.write(str(n + 1) + "\t" + next_seed.hexdigest())
    
    return pw.hexdigest()

""" # set the first password
with open(SEED_PATH, "w") as f:
    f.write(firstSeed)
 """

# Use the passwords from passwords.txt to crack the zip file backup_argv[1].zip
def crackZip(zipFile, password):
    try:
        zipFile.extractall(pwd=bytes(password, "utf-8"))
        print("Password found: " + password)
        return True
    except Exception as e:
        return False

def main():
    print("Cracking the zip file backup_" + sys.argv[1] + ".zip")
    zipFile = zipfile.ZipFile("backup_" + sys.argv[1] + ".zip")
    password = findZipPassword()
    if crackZip(zipFile, password):
        return
    print("Password not found")


if __name__ == "__main__":
    main()

    
