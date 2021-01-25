from waapi import WaapiClient
from pprint import pprint

try:
    # Connecting to Waapi using default URL
    with WaapiClient() as client:
        #生成容器
        select={"options":{"return": ["id", "name", "type"]}}
        selected_res=client.call("ak.wwise.ui.getSelectedObjects",select)["objects"]

        for i in selected_res:
            print(i["name"])
            bnk_new={
            "parent": "{7C99E8CC-D901-4D63-A698-E9E989CA221E}", 
            "type": "SoundBank", 
            "name": i["name"]      
            }
            soundbank_id = client.call("ak.wwise.core.object.create",bnk_new)
            pprint(soundbank_id)
            bnk_list ={
                    "operation":"add",
                    "inclusions":[{"filter":["media"],"object":i["id"]}],
                    "soundbank":soundbank_id["id"]
                    }        
            client.call("ak.wwise.core.soundbank.setInclusions",bnk_list)

except:
    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")