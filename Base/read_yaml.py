import os

import yaml

#
# class ReadYAML():
#     def __init__(self, filename):
#         self.filepath = os.getcwd() + os.sep + "Datapool" + os.sep + filename
#
#     def read_yaml(self):
#         with open(self.filepath, 'r', encoding='utf-8') as f:
#             return yaml.load(f)


class ReadYaml02():
    def read_yaml(self):
        with open("../DataPool/read_setting_yaml.yaml", "r", encoding="utf-8") as f:
            return yaml.load(f)
#
# #
if __name__ == '__main__':
    # print(ReadYAML('read_setting_yaml').read_yaml())
    print(ReadYaml02().read_yaml())
