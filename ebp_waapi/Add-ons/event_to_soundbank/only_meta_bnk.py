from waapi import WaapiClient

try:
    # Connecting to Waapi using default URL
    with WaapiClient() as client:
        #获取选择的obj信息
        select={"options":{"return": ["id", "name"]}}
        selected_res=client.call("ak.wwise.ui.getSelectedObjects",select)["objects"]
        #根据获取的obj信息，生成bnk
        for i in selected_res:
            print(i["id"])
        #将event添加进生成的bnk中，且只包含event和structures信息
            bnk_list ={
                    "operation":"add",
                    "inclusions":[{"filter":["events","structures"],"object":i["id"]}],
                    "soundbank":"{D08FCC68-A43D-425F-A011-51D2833F54F8}"
                    }        
            client.call("ak.wwise.core.soundbank.setInclusions",bnk_list)

except:
    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")