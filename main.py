from cmd import Cmd
import os
os.chdir('C:')
path = os.getcwd()
print(f'Your default directory is:{path}\n'
      f'Enter "help" for available commands')


class CommandPromt(Cmd):

    def do_exit(self, inp):
        print("Bye")
        return True

    def do_DirList(self, inp):
        dir_list = os.listdir()
        print(dir_list)

    def do_MoveToDir(self, inp):
        try:
            new_path = input('Enter new path:')
            os.chdir(new_path)
            os.getcwd()
            print(f"Now, your current directory is :{new_path}")
        except FileNotFoundError as e:
            print(f"Directory not found\n"
                  f"{e}")

    def do_OneDirBack(self, inp):
        os.chdir('C:')
        path2 = os.getcwd()
        print(path2)

    def do_BackToInitFolder(self, inp):
        os.chdir("..")
        path3 = os.getcwd()
        print(path3)

    def do_CurrentDir(self, inp):
        path4 = os.getcwd()
        print(path4)

    def do_CreateDir(self,inp):
        new_dir_name = input()
        os.getcwd()
        parent_dir = os.getcwd()
        path5 = os.path.join(parent_dir, new_dir_name)
        try:
            os.mkdir(path5)
        except OSError as error:
            print(error)

    def do_Rename(self,inp):
        oldname = input()
        newname = input()
        try:
            os.rename(oldname, newname)
        except FileNotFoundError as e:
            print(f"Please enter correct names\n"
                  f"{e}")
        os.rename(oldname, newname)
    def do_CreateFile(self,inp):
        new_file_name = input('Enter new name of file:')
        f = open(new_file_name, "w")

    def do_RemoveDir(self,inp):
        dir_name = input('Enter name of dir:')
        os.rmdir(dir_name)

    def do_RemoveFile(self,inp):
        dir_name = input('Enter name of file:')
        os.remove(dir_name)

    def do_ReadFile(self,inp):
        file_path = input('Enter a file path: ')

        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8-sig') as f:
                lines = f.readlines()
                print(lines)
        else:
            print('The specified file does NOT exist')

CommandPromt().cmdloop()

