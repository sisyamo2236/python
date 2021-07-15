
import sys
import zipfile
#-------------------------------------------------------- try unzip
def unzip_with_pw(filename, pw):
    with zipfile.ZipFile(filename, "r") as zip_file:
        try:
            zip_file.extractall(path="./", pwd=pw.encode())
            print("{} --- extraction is successful!".format(pw))
        except:
            print("{} --- wrong password!".format(pw))
            return False
    return True
#-------------------------------------------------------- main
# PW : 1234
#
if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print('usage: {} [zipFileName]'.format(args[0]))
    else:
        print(args[1])
        zip_filename = args[1]
        for i in range(10000):
            pw = "{:04d}".format(i)
            if unzip_with_pw(zip_filename, pw):
                sys.exit()
