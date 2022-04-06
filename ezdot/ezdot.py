from pathlib import Path
import json
import sys
import subprocess
import os
from ezdot.config import Config
import shutil
home_dir = Path.home()
current_dir = Path.cwd()
config_file_name = "ezdot.json"
config_dir_name = "ezdot"
config_default = {
    "files": [],
    "folders": [],
    "home_files": [],
    "home_folders": [],
    "home_symlink": [],
}
    # "dotfiles_dir": [home_dir / ".dotfiles"],
# }
dotfiles_dir = home_dir / ".dotfiles"

config_path = home_dir / ".config" / config_dir_name / config_file_name
cfg = Config(config_path, config_default)
if cfg.Setup():
    print('config setup success')
else:
    print('config setup failed, Continue y/n? ')
    answer = input()
    if answer == 'y':
        pass
    elif answer == 'n':
        cfg.error('cfg setup error')
commands = ["rm", "add", "addD", "addF","reset", "loadx", "load", "sync", "push", "help", "setup", "link", "pull", "add", "dlinkx","flinkx", "auto_setup", "default_setup", "folders","files","home_files","home_folders","home_symlink", "add_to_files", "add_to_folders" , "add_to_home_files", "add_to_home_folders", "add_to_home_symlink", "set_folders","set_files","set_home_files","set_home_folders","set_home_symlink", "add_to_files", "add_to_folders" , "add_to_home_files", "add_to_home_folders", "add_to_home_symlink", "backup_config"]
def main():
    try:
        user_input = sys.argv[1]
        uarg2 = sys.argv[2]
    except:
        pass
    else:
        cmd = user_input
        if cmd in commands:
            process(sys.argv)
        else:
            print("Invalid Cmd")
    try:
        user_input = sys.argv[1]
    except:
        print("not enough args")
    else:
        cmd = user_input
        if cmd in commands:
            process(sys.argv)
        else:
            print("Invalid Cmd")
def process(*argv):
    try:
        cmd = argv[0][1]
        arg2 = argv[0][2]
        print(argv, arg2, cmd)
    except:
        print(argv)
    if cmd == "link":
        if data:=cfg.Read():
            print('yesss')
            for x in data['home_files']:
                print(x)
                dotfiles_path_hf = Path(x)
                sync_dotfiles(dotfiles_path_hf)
            for x in data['files']:
                print(x)
                dotfiles_path_f = Path(x)
                sync_dotfiles(dotfiles_path_f)
            for x in data['home_folders']:
                print(x)
                dotfiles_path_hfo = Path(x)
                sync_home_folders(dotfiles_path_hfo)
            for x in data['folders']:
                print(x)
                dotfiles_path_fo = Path(x)
                symlink_dir(dotfiles_path_fo) 
            for x in data['home_symlink']:
                print(x)
                dotfiles_path_hs = Path(x)
                link_dir(dotfiles_path_hs) #links folders folder as single folder
        else:
            print('link config read error')
    elif cmd == "rm": #delF function to remove a path from config
        path = str(current_dir)
        changed = False
        if data:=cfg.Read():
            fi = data['files']
            fo = data['folders']
            z = data['home_symlink']
            x = data['home_files']
            y = data['home_folders']
            if path in x:
                x.remove(path)
                changed = True
                unsync_dotfiles(path)
            else:
                print('path not in files')
            if path in fi:
                fi.remove(path)
                changed = True
                unsync_dotfiles(path)
            else:
                print('path not in files')
            if path in fo:
                fo.remove(path)
                changed = True
                unsync_dotfiles(path)
                unlink_dir(Path(path))
            else:
                print('path not in files')
            if path in z:
                z.remove(path)
                changed = True
                unlink_dir(Path(path))
            if path in y:
                y.remove(path)
                changed = True
                unsync_dotfiles(path)
                unlink_dir(Path(path))
            else:
                print('path not in folders')
            if changed: 
                if cfg.Write(data):
                    print('rm worked\n', cfg.Read())
                else:
                    print('rm write error')
            else:
                print('no change')
        else:
            print('rm read error')
    elif cmd == "add":
        path = str(current_dir)
        print(path)
        if data:=cfg.Read():
            x = data['files']
            if path not in x:
                x.append(path)
                print(data, x)
                if cfg.Write(data):
                    print('added\n', cfg.Read())
            else:
                print('path already added')
        else:
            print('add read error')
    elif cmd == "addF":
        path = str(current_dir)
        if data:=cfg.Read():
            x = data['files']
            if path not in x:
                x.append(path)
                if cfg.Write(data):
                    print('added F\n')
                else:
                    print('addF write error')
            else:
                print('path already added F')
        else:
            print('addF read error')
    elif cmd == "home_symlink" or cmd == "set_home_symlink":
        path = str(current_dir)
        if data:=cfg.Read():
            x = data['home_symlink']
            if path not in x:
                x.append(path)
                if cfg.Write(data):
                    print('addedD F\n', cfg.Read())
                else:
                    print('addD write error')
            else:
                print('path already added D')
        else:
            print('addD read error')
    elif cmd == "home_folders" or cmd == "set_home_folders":
        path = str(current_dir)
        if data:=cfg.Read():
            x = data['home_folders']
            if path not in x:
                x.append(path)
                if cfg.Write(data):
                    print('addedD F\n', cfg.Read())
                else:
                    print('addD write error')
            else:
                print('path already added D')
        else:
            print('addD read error')
    elif cmd == "folders" or cmd == "set_folders":
        path = str(current_dir)
        if data:=cfg.Read():
            x = data['folders']
            if path not in x:
                x.append(path)
                if cfg.Write(data):
                    print('addedD F\n', cfg.Read())
                else:
                    print('addD write error')
            else:
                print('path already added D')
        else:
            print('addD read error')
    elif cmd == "home_files" or cmd == "set_home_files":
        path = str(current_dir)
        if data:=cfg.Read():
            x = data['home_files']
            if path not in x:
                x.append(path)
                if cfg.Write(data):
                    print('addedD F\n', cfg.Read())
                else:
                    print('addD write error')
            else:
                print('path already added D')
        else:
            print('addD read error')
    elif cmd == "files" or cmd == "set_files":
        path = str(current_dir)
        if data:=cfg.Read():
            x = data['files']
            if path not in x:
                x.append(path)
                if cfg.Write(data):
                    print('addedD F\n', cfg.Read())
                else:
                    print('addD write error')
            else:
                print('path already added D')
        else:
            print('addD read error')
    elif cmd == "add_to_files":
        src = arg2
        if data:=cfg.Read():
            dst = data['files'][0]
            copy_to(src, dst)
    elif cmd == "add_to_folders":
        src = arg2
        if data:=cfg.Read():
            dst = data['folders'][0]
            # dst = data['folers'][0]
            copy_to(src, dst)
    elif cmd == "add_to_home_files":
        src = arg2
        print(src)
        if data:=cfg.Read():
            dst = data['home_files'][0]
        copy_to(src, dst)
    elif cmd == "add_to_home_folders":
        src = arg2
        if data:=cfg.Read():
            dst = data['home_folders'][0]
            copy_to(src, dst)
    elif cmd == "add_to_home_symlink":
        src = arg2
        if data:=cfg.Read():
            dst = data['home_symlink'][0]
            copy_to(src, dst)
    elif cmd == "backup_config":
        if data:=cfg.Read():
            dst = data['files'][0]
        copy_to(config_path, dst) 
    elif cmd == "addD":
        path = str(current_dir)
        if data:=cfg.Read():
            x = data['folders']
            if path not in x:
                x.append(path)
                if cfg.Write(data):
                    print('addedD F\n', cfg.Read())
                else:
                    print('addD write error')
            else:
                print('path already added D')
        else:
            print('addD read error')
    elif cmd == "reset":
        cfg.Reset()
    elif cmd == "load":
        file = current_dir / ".config" / "ezdot" / "ezdot.json"
        cfg.Load(file)
    elif cmd == "loadx":
        user_input = input("Enter Config Path: ")
        file = current_dir / Path(user_input)
        cfg.Load(file)
    elif cmd == "flinkx":
        dotfiles_path = current_dir
        sync_dotfiles(dotfiles_path)
    elif cmd == "dlinkx":
        dotfiles_path = current_dir #add support for symlinking folders
        symlink_dir(dotfiles_path)
    elif cmd == "upload":
            # if config_path.is_file():  # add check if empty here
                # dotfiles_path = config_path.read_text()
        dotfiles_path = dotfiles_dir
        cmdout = subprocess.run(
            ["git", "add", "."], cwd=dotfiles_path, stdout=subprocess.PIPE
        ).stdout.decode("utf-8")
        print(cmdout)
        cmdout = subprocess.run(
            ["git", "commit", "-m", '"ezdot dotfile update"'],
            cwd=dotfiles_path,
            stdout=subprocess.PIPE,
        ).stdout.decode("utf-8")
        print(cmdout)
        cmdout = subprocess.run(
            ["git", "push"], cwd=dotfiles_path, stdout=subprocess.PIPE
        ).stdout.decode("utf-8")
        print(cmdout)
        print("UPLOADED")
        # return False
            # else:
                # print("Empty Config")
                # return False
    elif cmd == "push":
        if config_path.is_file():  # add check if empty here
            dotfiles_path = config_path.read_text()
            cmdout = subprocess.run(
                ["git", "add", "."], cwd=dotfiles_path, stdout=subprocess.PIPE
            ).stdout.decode("utf-8")
            print(cmdout)
            cmdout = subprocess.run(
                ["git", "commit", "-m", '"dotfile update"'],
                cwd=dotfiles_path,
                stdout=subprocess.PIPE,
            ).stdout.decode("utf-8")
            print(cmdout)
            cmdout = subprocess.run(
                ["git", "push"], cwd=dotfiles_path, stdout=subprocess.PIPE
            ).stdout.decode("utf-8")
            print(cmdout)
            print("UPLOADED")
            return False
        else:
            print("Empty Config")
            return False
    elif cmd == "help":
        print(commands)
    elif cmd == "setup":
        directory_name = current_dir
        dotfiles_path = directory_name.resolve()
        if config_path.is_file():
            config_path.write_text(str(dotfiles_path))
            return
        else:
            config_parent = config_path.parent
            config_parent.mkdir(parents=True, exist_ok=True)
            config_path.touch()
            config_path.write_text(str(dotfiles_path))
            return
    else:
        print("Cmd !Exist")
def copy_to(src, dst):
    shutil.copy(src, dst)  # dst can be a folder; use shutil.copy2() to preserve timestamp
def symlink_dir(dotfiles_path):
    directories=[d for d in os.listdir(dotfiles_path) if os.path.isdir(d)]
    for y in directories:
        dir_name = y
        dir_in = dotfiles_path / Path(y)
        dir_out = home_dir / dir_name
        setup_sym_dir(dir_out, dir_name)
        make_links(dir_in, dir_out)
        print("Synced Dirs")
def link_dir(dotfiles_path):
    dir_name = dotfiles_path.name
    dir_in = dotfiles_path
    dir_out = home_dir / dir_name
    setup_sym_dir(dir_out, dir_name)
    make_links(dir_in, dir_out)
    print("Synced Dirs")
def unlink_dir(dotfiles_path):
    dir_name = dotfiles_path.name
    dir_in = dotfiles_path
    dir_out = home_dir / dir_name
    unlink_file(dir_out)
    restore_old_dir(dir_out, dir_name)
def setup_sym_dir(thefile, name):
    if thefile.is_symlink():
        thefile.unlink()
    else:
        pass
    if thefile.is_dir():
        rename_dir(thefile, name)
    else:
        pass
def rename_dir(thefile, name):
    fullname = thefile
    fname = name
    fdir = thefile.parents[0]
    new_name = Path(str(fname) + "_old")
    path_old = fdir / new_name
    if thefile.is_dir():
        fullname.rename(path_old)
    else:
        pass
def restore_old_dir(thefile, name):
    fullname = thefile
    fname = str(name) + "_old"
    fdir = thefile.parents[0]
    new_name = Path(fname)
    path_old = fdir / new_name
    if path_old.exists():
        path_old.rename(fullname)
    else:
        pass
def unrename_old_file(thefile):
    fullname = thefile
    fname = thefile.stem
    fsuffix = thefile.suffix
    fdir = thefile.parents[0]
    new_name = Path(fname + "_old" + fsuffix)
    path_old = fdir / new_name
    if path_old.exists():
        path_old.rename(fullname)
def sync_dotfiles(dotfiles_path):
    if check_exist(dotfiles_path):
        dots_all = dotfiles_path.rglob("*")
        dots_list = [x for x in dots_all]
        dots_files = [x for x in dots_list if x.is_file()]
        dots_dirs = [x for x in dots_list if x.is_dir()]
    else:
        print("Invalid Directory")
        return False
    for y in dots_dirs:
        dir_in = Path(y)
        dir_name = dir_in.relative_to(dotfiles_path)
        dir_out = home_dir / dir_name
        check_dir(dir_out)
    for x in dots_files:
        dot_in = Path(x)
        dot_name = dot_in.relative_to(dotfiles_path)
        dot_out = home_dir / dot_name
        check_file(dot_out)
        make_links(dot_in, dot_out)
        print("Synced Dotfiles")
def sync_home_folders(dotfiles_path):
    if check_exist(dotfiles_path):
        dots_all = dotfiles_path.rglob("*")
        dots_list = [x for x in dots_all]
        dots_files = [x for x in dots_list if x.is_file()]
        dots_dirs = [x for x in dots_list if x.is_dir()]
    else:
        print("Invalid Directory")
        return False
    for y in dots_dirs:
        dir_in = Path(y)
        dir_name = dir_in.relative_to(dotfiles_path)
        dir_out = home_dir / dir_name
        print(dir_in,dir_name,dir_out)
        try:
            if not Path(dir_out).exists():
                Path(dir_out).symlink_to(dir_in)
                print(' LINKED ')
        except:
            pass
def check_home_fo(thefile, dir_name):
    if thefile.is_symlink():
        pass
    else:
        pass
    if thefile.is_dir():
        print('file is a dir')
    else:
        pass
def make_links(dotin, dotout):
    dotout.symlink_to(dotin)
def unsync_dotfiles(dotfiles_p):
    dotfiles_path = Path(dotfiles_p)
    dots_all = dotfiles_path.rglob("*")
    dots_list = [x for x in dots_all]
    dots_files = [x for x in dots_list if x.is_file()]
    dots_dirs = [x for x in dots_list if x.is_dir()]
    for y in dots_dirs:
        dir_in = Path(y)
        dir_name = dir_in.relative_to(dotfiles_path)
        print(dir_name)
        dir_out = home_dir / dir_name
        unlink_file(dir_out)
        restore_old_dir(dir_out, dir_name)
    for x in dots_files:
        dot_in = Path(x)
        dot_name = dot_in.relative_to(dotfiles_path)
        dot_out = home_dir / dot_name
        unlink_file(dot_out)
        unrename_old_file(dot_out)
    print("UNSynced Dotfiles")
def unlink_file(thefile):
    if thefile.is_symlink():
        thefile.unlink()
    else:
        pass
def check_file(thefile):
    if thefile.is_symlink():
        thefile.unlink()
    else:
        pass
    if thefile.is_file():
        rename_old(thefile)
    else:
        pass
def check_dir(thedir):
    if thedir.is_dir():
        pass
    else:
        thedir.mkdir(parents=True, exist_ok=True)
def rename_old(thefile):
    fullname = thefile
    fname = thefile.stem
    fsuffix = thefile.suffix
    fdir = thefile.parents[0]
    new_name = Path(fname + "_old" + fsuffix)
    path_old = fdir / new_name
    fullname.rename(path_old)
def check_exist(usrdir):
    if usrdir.is_dir():
        return True
    else:
        return False
if __name__ == "__main__":
    main()
