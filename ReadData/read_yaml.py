import yaml
def read_yaml():
    with open("../Datapool/yaml.yaml", 'r', encoding="utf-8")as f:
        dats = yaml.load(f)
        return dats

taml=read_yaml()
print(taml)