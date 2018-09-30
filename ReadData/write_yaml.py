import yaml

data = {"data":
            {'data1': {'name': '张三', 'age': 18}, 'data2': {'name': '李四', 'age': 10}}}


def write_yaml():
    with open('../Datapool/write_yaml.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(data, stream=f, encoding='utf-8', allow_unicode=True)


write_yaml()
