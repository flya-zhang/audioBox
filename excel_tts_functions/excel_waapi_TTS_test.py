from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint
import excel_value as ev


#创建一个argumentparser的对象

try:
    # Connecting to Waapi using default URL
    with WaapiClient() as client:              
        selected  = client.call("ak.wwise.ui.getSelectedObjects")['objects']
        if len(selected) != 1:
            raise Exception("不能选择多个")
        parent_id = selected[0]['id']
        # 生成容器
        print("create contianer:")

        for i in range(2,ev.num_of_dialogue()):
            i = str(i)
            temp_name = 'B'+i
            temp_note = 'C'+i            
            str_1=ev.row_value(temp_name)
            str_2=ev.row_value(temp_note)
            create_object = {
                "name":str_1,
                "parent":parent_id, 
                "type":"Sound",
                "notes":str_2                       
                }
            res = client.call("ak.wwise.core.object.create", create_object)
            #导入note信息
            note_info={
                "object":res['id'],
                "value":str_2
            }
            client.call("ak.wwise.core.object.setNotes", note_info)

        os.system("python或python3 xxx.py")
        
        
except CannotConnectToWaapiException:
    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")








