import xlwings as xl
import original_to_json

#与已有的excel文件相关联
wb = xl.Book('audio_AssetTracker.xlsx') 
#表头内容
table_val=["files name","trigger","container","envnt","bnk"]
original_struct=original_to_json.original_datastruct("F:\\code\\ebp_waapi\\original")
#将文件内容从第二行开始，填进表格中
for key in original_struct:#创建sheet    

    sht=wb.sheets.add(key)
    sht.select()

    #创建template,将表头填在第一行里
    for j,k in enumerate(table_val):
        sht.range(str(chr(ord("A")+j)+"1")).value=k
        #设置表头颜色
        sht.range(str(chr(ord("A")+j)+"1")).color=(48,181,117)
        #设置表头字体颜色
        sht.range(str(chr(ord("A")+j)+"1")).api.Font.Color = 0xFFFFFF
        #设置表头字体为加粗
        sht.range(str(chr(ord("A")+j)+"1")).api.Font.Bold = True

    #填写files字典内的内容    
    for index,val in enumerate(original_struct[key]):
        if type(val)==dict:                                          
            sht.range("A"+str(index+2)).raw_value=list(val.keys())[0]                     
            sht.range("A"+str(index+2)).color=(73,128,249)
            sht.range("A"+str(index+2)).api.Font.Color = 0xFFFFFF             
        else:
            sht.range("A"+str(index+2)).raw_value=val

#使用插值的形式，将container的内容插回excel中    
    for val_2 in original_struct[key]:
        if type(val_2)==dict:
            #设定需要查找的关键词
            search_kw = list(val_2.keys())[0]
            print(search_kw)
            #从第一行开始，直到有内容的最后一行，查找关键词所在行，返回该行序号
            for c_row in range(2,sht.range('A' + str(sht.cells.last_cell.row)).end('up').row+1):
                if search_kw in str(sht.range('A{}'.format(c_row)).value):
                    search_kw_row=sht.range('A{}'.format(c_row)).row
                    print(search_kw_row)
                    #定义预先插入多少行
                    for emptyrow_num in range(1,len(list(val_2.values())[0])+1):
                        sht.range("A"+str(search_kw_row++1)).insert()
                    #在插入的空白行中，依次填入container的数据
                    for index_2,value_2 in enumerate(list(val_2.values())[0]):                            
                        sht.range("A"+str(search_kw_row+(index_2+1))).value=value_2
                        #将新增行的颜色设置为无色
                        sht.range("A"+str(search_kw_row+(index_2+1))).api.Font.Color = 0x000000
                        sht.range("A"+str(search_kw_row+(index_2+1))).color=None
        if type(val_2)!=dict:
            continue
    #自动根据数据长度去调整格子的长度
    sht.autofit()


    