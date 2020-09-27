import xlwings as xw
#获取对应的行，列的值
excel = xw.Book('D:\\code\\excel_test\\dialogue.xlsx')
sht = excel.sheets["vox"]

def num_of_dialogue():   
    leng = list(sht.used_range.shape)
    #excel第一行要留空或不包含有用数据
    n_d = leng[0]-1
    return n_d

def row_value(row_num):    
    r_v=sht.range(row_num).value
    return r_v

def column_value(column_num):    
    c_v=sht.range(column_num).value
    return c_v







