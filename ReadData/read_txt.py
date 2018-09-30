def read_txt():
    with open("../Datapool/txt",'r',encoding="utf-8")as f:
        datas = f.readlines()
        arrs = []
        for data in datas:
            arrs.append(data.strip().split(","))
        return arrs
print(read_txt())