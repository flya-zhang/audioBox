import json
import os

#获取oringinal文件夹的路径
def original_datastruct(abspath):
    original_address = abspath
    category=os.listdir(original_address)

    #将original文件夹里面的所有内容成字典
    files={}
    container={}
    for i in category:
        temp={i:os.listdir(original_address+"/"+i)}
        files.update(temp)

    #遍历内层文件是否为files
        with os.scandir(original_address+"/"+i) as entries:
            #若内层文件时文件夹，则将该文件夹当成container，组成新的字典    
            for index,entry in enumerate(entries): 
                if entry.is_dir():           
                    container={entry.name:[j for j in os.listdir(entry.path)]}
                    #将原列表内的元素，替换成新生成的字典               
                    files[i][index]=container
                elif entry.is_file():
                    continue
                else:           
                    print("original的结构不规范")
                    break

    #创建json文件,并按照json样式可视化显示
    original_json=json.dumps(files,indent=1)
    with open("original_value.json","w") as obj:
        obj.write(original_json)
    #返回字典的数据结构
    return files
