#!/bin/python
import json
import sys
from emoji import is_emoji 

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


def show_info(vid):
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

    print("Video ID : ", vid)
    print(cname)
    print(tags, "\n")
    print(title)
    print(desc)
    print("View:%d, Like:%d, Dislike: %d"%(vc, vlc, vdc))

    cn = vid_json["data"].get("comm_n", 0)
    print("Comment Count : %d"%(cn)) 
    print("\n---")
    index = 0
    cmts = vid_json["data"]["comments"][index]
    
    curr = 0
    for cmts in vid_json["data"]["comments"]:
       
        for ocmt in cmts["items"]:
            cmt = ocmt["snippet"]["topLevelComment"]["snippet"]
            
            an = cmt["authorDisplayName"]
            text = cmt["textOriginal"]
            text = toEnglish(text)
            lc =int(cmt["likeCount"])
            dt = cmt["publishedAt"] 
            rc =int(ocmt["snippet"]["totalReplyCount"])
            
            print(an)
            print(text) 
            print("Like:%d, RepliesCount:%d"%(lc, rc))
            
            print("---")

vid = sys.argv[1]
show_info(vid)
