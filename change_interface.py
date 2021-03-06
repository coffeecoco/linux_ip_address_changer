####################################################################
#
# 	Creator 	: Egbie Anderson
# 	Purpose 	: interface changer
# 	Language 	: python 2.xx
#       OS              : <Linux >
#       Date  created   : 6 may 2012
#       
#       Original written to be used with Backtrack but can be used
#       with any linux box. The purpose for the script is to set
#       my dnaymic ip address into a static ip address enabling me to sync
#       my many virtual machines into one network. And also allow me to go
#       back to my original dynamic ip address. Purpose this will enable to
#       learn how to hack using backtrack.
#
#######################################################################


#!/usr/bin/env python
import optparse
import os
import shutil
from time import sleep

class ChangeInterfaces(object):
    """
    The program replaces the interfaces file located at /etc/
    it with whatever new file the user decides it should be.
    """

    def __init__(self):
        """the constructor method"""
        
        # the location of the interface file
        self.interface_file = "/etc/network/interfaces" # interface file in a linux machine
        self.file_location = "/root/Desktop/"           # location to store the backup interface file in Backtrack

    
    def create_backup(self):
        """create a backup of the orignal file interface"""
       
        self.backup_name = 'interface_file.backup'
        
        print "\n[+] please wait checking if there is a backup up file"
        if os.path.exists(os.path.join(self.file_location, self.backup_name)):

          print "[+] backup file does not exist, please wait creating backup file"
          
          # take the orignal interface file and makes a backup copy
          shutil.copyfile(self.interface_file, "/etc/network/interface_file.backup")
          print "[+] backup file successful created"

        else:
          print "[+] backup file found, no need to created backup file"
        
    def replace_file(self, replace_file_with):
        """replace the orignal interface file with a new interface file"""
        
        self.new_file = self.file_location + replace_file_with
        self.create_backup()
        print "[+] please wait attempting to replacing file.."
        sleep(1)
        
        # replace the file self.interface_file with the new file
        
        try:
            shutil.copyfile(self.new_file, self.interface_file)
            print "[+] file successfully replaced\n"

        except IOError:
           print "[+] The interface file your trying to load does not exit !!"
           print "[!] Exiting!!!"
           exit(0)

    def reboot_network(self):
        """reboots the network"""
        
        print "[+] please wait reboot network.."
        sleep(1)
        os.system("/etc/init.d/networking restart")
		
 
def main():
 
   changeInterfaces = ChangeInterfaces()
   
   parser = optparse.OptionParser("usage%prog -f <file to be used for replacing>")
   parser.add_option("-f", dest = "interface_file", type = "string", help = "the file that will be used to replace the interface file")
   options, args = parser.parse_args()
      
   if (options.interface_file == None):
      print parser.usage
      exit(0)
   else:
      
     changeInterfaces.replace_file(options.interface_file) # replace the orignal interface file with the new interface
     changeInterfaces.reboot_network()                     # reboots the network to start the new interface
	
# when invoked calls the main function
if __name__ == "__main__":
   main()
  
