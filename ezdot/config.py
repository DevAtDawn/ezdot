import pathlib
from pathlib import Path
import json
class Config:
    home_path = Path.home()
    cwd_path = Path.cwd()
    def __init__(self, config_path='', config_default=''):
        self.config_path = config_path
        self.config_default = config_default
    def setDefault(self, default):
        self.config_default = default
    def getDefault(self):    
        return self.config_default
    def setConfig(self, cfg):
        self.config_path = cfg
    def getConfig(self):    
        return self.config_path 
    def Setup(self):    
        return self.setup_config(self.config_path, self.config_default) 
    def Reset(self):    
        return self.reset_config(self.config_path, self.config_default)
    def Read(self):    
        return self.read_config(self.config_path)
    def Load(self, file):    
        return self.load_config(self.config_path, self.config_default, file) 
    def Write(self, data):    
        return self.write_config(self.config_path, data)
    def error(self, msg):
        raise Exception(msg)
    def read_config(self, cfg): #read_json
        try:
            with open(cfg) as f:
                data = json.load(f)
        except:
            print('read config error')
            return False
        else:
            print(data)
            return data
    def write_config(self, cfg, txt): #write_json
        try:
            with open(cfg, 'w') as json_file:
                json.dump(txt, json_file)
        except:
            print('Write Config error')
            return False
        else:
            print('Write Config success')
            return True
    def exists_config(self, cfg):
        if cfg.exists(): return True
        else: return False
    def make_config(self, cfg):
        cfg_parent = cfg.parent
        cfg_parent.mkdir(parents=True, exist_ok=True)
        cfg.touch()
    def validate_config(self, cfg, txt):
        d = self.read_config(cfg)
        if not d:
            return False
        else:
            if d.keys() == txt.keys():
                print("Matches")
                return True
            else:
                print('Doesnt Match', d, txt)
                return False
    def setup_config(self, cfg, txt):
        if self.exists_config(cfg) and self.validate_config(cfg, txt):
            print("valid")
            return True
        else:
            print("setting up")
            if self.reset_config(cfg, txt):
                print("done")
                return True
            else:
                print("setup reset error")
                return False
    def reset_config(self, cfg, txt): #.exists():
        self.make_config(cfg)
        if self.exists_config(cfg):
            self.write_config(cfg, txt)
            if self.validate_config(cfg, txt):
                return True
            else:
                self.error('Reset Validate Error')
        else:
            self.error('Reset Make Error')
    def del_config(self, cfg):
        if self.exists_config(cfg):
            cfg.unlink()
            print('removed')
        else:
            print('!exist')
    def load_config(self, cfg, txt, file):
        f_path = Path(file)
        if self.exists_config(f_path):
            text = self.read_config(f_path)
        else:
            print('invalid file path')
            return False
        if not text:
            print('invalid config, writing defaults')
            self.write_config(f_path, txt)
            return False
        else:
            self.del_config(cfg)
            self.make_config(cfg)
            if self.exists_config(cfg):
                self.write_config(cfg, text)
                if self.validate_config(cfg, txt):
                    return True
                else:
                    self.error('Load Validate Error')
            else:
                self.error('Load Make Error')
