#!/usr/bin/python3
#Aaron Noller & Paul Schartung
#Lab08

import os
import sys
import hashlib

ignore_list = ["/dev", "/proc", "/run", "/sys", "/tmp", "/var/lib", "/var/run"]

def main():
   for root, dirs, files in os.walk(".", topdown=True): #from geeksforgeeks.org
      # if root not in ignore_list:

     testlist = root.split("/")
     for directory in testlist:
         if directory not in ignore_list:
             print(root)
             #######STACK OVERFLOW######
             for f in files:
                current_file = os.path.join(root,f)
                H = hashlib.sha256()
                with open(current_file, "rb") as FIN:
                    H.update(FIN.read())
                    with open("gethashes.txt", "a+") as myfile:
                        myfile.write(current_file),myfile.write("\n"),myfile.write("            "),myfile.write(H.hexdigest()),myfile.write("%s\n")
            ##############################################
               # print(dirs)
               # print(files)
               # print(hashlib.SHA256( ))
                print("-----------------------------------------")


#hashlib.SHA256(file)



if __name__ == "__main__":
   main()
