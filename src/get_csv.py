#!/bin/python
import json
import sys
from emoji import is_emoji 
import re
import pandas as pd


def isValidText(text):
    for char in text:
        if isValidCharacter(char) < 0: return (False, char)
    return (True, None)
def isValidCharacter(char):
    ret = -1
    try:
        char.encode("utf-8").decode("ascii")
        ret = 0
    except:
        if is_emoji(char) : ret = -1
    return ret

def toEnglish(text):
    text2 = ""
    for char in text:
        if isValidCharacter(char) == 0: text2 += char.encode("utf-8").decode("ascii")
    return text2


rows = [ ["date", "name", "comment", "like", "replies"] ]  

def get_csv(vid):
    global rows
    
    data = {
        "date" :    [],
        "name" :    [],
        "comment":  [],
        "like" :    [],
        "replies":  []
    }
    
    file = open("%s"%vid)
    vid_json = json.load(file)
    vinfo_t = vid_json["data"]["ss_data"]["items"][0]["snippet"]
    vinfo_s = vid_json["data"]["ss_data"]["items"][0]["statistics"]
    title=vinfo_t["title"]
    desc=vinfo_t["description"]
    cname=vinfo_t["channelTitle"]
    tags="|".join(vinfo_t.get("tags", []))
    vc = int(vinfo_s["viewCount"])
    vlc =int(vinfo_s["likeCount"])
    vdc = int(vinfo_s["dislikeCount"])
    
    cn = vid_json["data"].get("comm_n", 0)
     
    index = 0
    cmts = vid_json["data"]["comments"][index]
    
    curr = 0
    for cmts in vid_json["data"]["comments"]:
       
        for ocmt in cmts["items"]:
            cmt = ocmt["snippet"]["topLevelComment"]["snippet"]
            
            an = cmt["authorDisplayName"]
            text = cmt["textOriginal"]
            text = toEnglish(text)
            text = text.replace("\n", " ").replace("\"", "\\\"")
            dt = cmt["publishedAt"] 
            lc =int(cmt["likeCount"])
            rc = int(ocmt["snippet"]["totalReplyCount"])
            data["date"]    +=  [ dt ]
            data["name"]    +=  [ an ]
            data["comment"] +=  [ text ]
            data["like"]    +=  [ lc ]
            data["replies"] +=  [ rc ]
    df = pd.DataFrame(data)
    df.to_csv("%s.csv"%vid)
    print(df)
vid = sys.argv[1]
get_csv(vid)
