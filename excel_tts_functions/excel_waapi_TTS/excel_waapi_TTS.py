import xlwings as xw
from waapi import WaapiClient, CannotConnectToWaapiException
from pprint import pprint


#excel表格查询
wb = xw.Book('D:\\code\\excel_test\\dialogue.xlsx')
sht = wb.sheets["sheet1"]
lis = list(sht.used_range.shape)
num_row = lis[0]-1

#这里print出来的字符串有问题
try:
    # Connecting to Waapi using default URL
    with WaapiClient() as client:
        # NOTE: client will automatically disconnect at the end of the scope
        
        # == Simple RPC without argument
        print("Getting Wwise instance information:")
        
        result = client.call("ak.wwise.core.getInfo")        
        pprint(result)        
        # == RPC with arguments
        print("Query the text:")      
        object_get_args = {
            "from": {
                "path": ["\\Actor-Mixer Hierarchy\\dialogue"]
            },
            "options": {
                "return": ["id", "name", "type"]
            }
        }
        result = client.call("ak.wwise.core.object.get", object_get_args)
        pprint(result)
        # for j in resual[return]:
        #     obj_id = j['id'] if j['id'] else contitune
        # #生成容器
        # print("create contianer:")
        # for i in range(2,num_row):
        #     i = str(i)
        #     temp = 'B'+i
        #     print(temp)
        #     str_1=sht.range(temp).value 
        #     create_object = {
        #         "parent":obj_id
        #         # "parent": "{5C8E0702-7108-4DE2-90E5-001C341847C6}", 
        #         "type": "Sound", 
        #         "name": str_1              
        #         }
        # #查询生成的容器ID           
        #     resual_1 = client.call("ak.wwise.core.object.create",kwargs = create_object)
        #     setting_note = {
        #         "object": "{A076AA65-B71A-45BB-8841-5A20C52CE727}", 
        #         "value": "This object's notes are set."
            # }

        
except CannotConnectToWaapiException:
    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")








