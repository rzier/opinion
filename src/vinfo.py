#!/bin/python
import json
import sys

def dump_info(vid):
    file = open("../data/%s/%s.json"%(vid, vid))
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

    final='''%s
title:%s
channel name:%s
view count:%d
like count:%d
dislike count:%d
comments count:%d
tags:%s
description:%s
    '''%(vid, title, cname, vc, vlc, vdc, cn,tags, desc)
    op = open("../data/%s/video_info.txt"%(vid), "w")
    op.write(final)
    op.close()
vid = sys.argv[1]
dump_info(vid)
