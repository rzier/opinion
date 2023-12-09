#!/bin/python
'''

Data Science Project Opinion
Rzier


Fetch Comments
Fetch Snippets
https://www.googleapis.com/youtube/v3/videos?key=<api_key>&id=<vid>&part=snippet
Fetch Like and Dislike
https://www.googleapis.com/youtube/v3/videos?key=<api_key>&id=<vid>8&part=statistics,snippet

Dislike Info
https://returnyoutubedislikeapi.com/votes?videoId=YbJOTdZBX1g


Reference:
- [Youtube Docs](https://developers.google.com/youtube/v3)
- [Generate API Key](https://console.cloud.google.com/getting-started?pli=1)

'''
from urllib import request as req
from dotenv import load_dotenv
import os
import json
import sys

load_dotenv()

api_key=os.getenv("api_key")
print(len(api_key if "API KEY Loaded !!" else "API Key Failed"))
vid=""
max_fetchable_comments = 100
def ycurl(api_key, vid, mres, pt=None):
    if mres > max_fetchable_comments:
        print("Maximum 100 Comments Allowed At Once")
    mres = min(mres, max_fetchable_comments)
    if not pt :
        return "https://www.googleapis.com/youtube/v3/commentThreads?key=%s&textFormat=plainText&part=snippet&videoId=%s&maxResults=%d"%(api_key, vid, mres)
    return "https://www.googleapis.com/youtube/v3/commentThreads?key=%s&textFormat=plainText&part=snippet&videoId=%s&maxResults=%d&pageToken=%s"%(api_key, vid, mres, pt)

ug = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"

def fetch_video_info(api_key, vid):
    url_ss = "https://www.googleapis.com/youtube/v3/videos?key=%s&id=%s&part=snippet,statistics"%(api_key, vid)
    dislikecount = -1;
    try:
        url_d = "https://returnyoutubedislikeapi.com/votes?videoId=%s"%(vid)
        print("Using Third Party To Fetch Dislike %s"%url_d)
        rq = req.Request(url_d)
        rq.add_header("User-Agent", ug)
        res = req.urlopen(rq)
        if res.status != 200:
            print("[ERROR]: Failed Dislike Fetch, Host Failed");
        else:
            data = json.loads(res.read())
            dislikecount = data["dislikes"]
    except Exception as e:
        print("[ERROR]: Failed Dislike Fetch %s"%e);
    res = req.urlopen(url_ss)
    ss_data = json.loads(res.read())
    ss_data["items"][0]["statistics"]["dislikeCount"] = dislikecount
    
    return ss_data


def fetch_video_comments(api_key, vid, fetch_comment_count):
    comments = []
    comm_n = 0
    pageToken = None
    if fetch_comment_count <= 0:
        fetch_comment_count = sys.maxsize
    try:
        while True:
            gurl = ycurl(api_key, vid, fetch_comment_count, pageToken)
            print("[INFO] Fetching... %s"%gurl)
            res = req.urlopen(gurl)
            if res.status != 200:
                print("%d Failed!\n"%res.status)
                return None
            data = res.read()
            pdata = json.loads(data)
            comments += [pdata]
            pageToken = pdata.get("nextPageToken", None)
            comment_fetched = pdata["pageInfo"]["totalResults"]
            comm_n += comment_fetched
            fetch_comment_count -= comment_fetched
            print("[INFO]: Fetched Comments : %d - %d - %d"%(comm_n, comment_fetched, fetch_comment_count)) 
            if pageToken == None or fetch_comment_count <= 0 or comment_fetched <= 0 : break
    except Exception as e:
        print("[ERROR]: %s"%e)
    return (comm_n, comments)


def isFileExist(filename):
    try:
        f = open(filename, "r")
        f.close()
        return True
    except:
        return False
    return False
def _cached_fetch_video_comments(api_key, vid, comment_count):
    '''
    This Function Ensures To Cache Comments In vid.json file
    '''
    cache = None
    try:
        com = fetch_video_comments(api_key, vid, comment_count)
        comm_n, comments = com
        file_name = "../data/%s.json"%(vid)
        fileExist = isFileExist(file_name)

        if fileExist :
            fcache_r = open(file_name, "r")
            cache = json.loads(fcache_r.read())
            cache["labels"] = list(set(cache["labels"] + [ "comments" ]))
            cache["data"]["comments"] = comments
            cache["data"]["comm_n"] = comm_n
            fcache_r.close()
    
        if cache :        
            file_data = json.dumps(cache)
            fcache_w = open(file_name, "w")
            fcache_w.write(file_data)
            fcache_w.close()
        else:
            cache = {}
            cache["labels"] = [ "comments" ]
            cache["data"] = {}
            cache["data"]["comments"] = comments
            cache["data"]["comm_n"] = comm_n
            file_data = json.dumps(cache)
            fcache_w = open(file_name, "w")
            fcache_w.write(file_data)
            fcache_w.close()


        print("Fetched %d Comments and Cached"%comm_n)
    except Exception as e:
        print("[ERROR]: in _cached_fetch_video_comments %s"%e)

    return cache
def _cached_fetch_video_info(api_key, vid):
    '''
    This Function Ensures To Cache Infpo In vid.json file
    '''
    cache = None
    try:
        ss_data = fetch_video_info(api_key, vid)
        file_name = "../data/%s.json"%(vid)
        fileExist = isFileExist(file_name)

        if fileExist :
            fcache_r = open(file_name, "r")
            cache = json.loads(fcache_r.read())
            cache["labels"] += [ "ss_data" ]
            cache["data"]["ss_data"] = ss_data 
            fcache_r.close()
    
        if cache :        
            file_data = json.dumps(cache)
            fcache_w = open(file_name, "w")
            fcache_w.write(file_data)
            fcache_w.close()
        else:
            cache = {}
            cache["labels"] = [ "ss_data" ]
            cache["data"]["ss_data"] = ss_data
            file_data = json.dumps(cache)
            fcache_w = open(file_name, "w")
            fcache_w.write(file_data)
            fcache_w.close()


        print("[INFO]: Fetched %d Vido Info and Cached")
    except Exception as e:
        print("[ERROR]: in _cached_fetch_video_info %s"%e)
    return cache


def cached_fetch_video_comments(api_key, vid, comment_count, refetch=False):
    file_name = "../data/%s.json"%(vid)
    cache = None
    try:
        file = open(file_name, "r")
        file_data = file.read()
        cache = json.loads(file_data)
        valid_cache = False
        valid_cache = "comments" in cache["labels"]
        print("[INFO]: Found Cache ../data/%s.json "%(vid))
        if valid_cache == False:
            print("[INFO]: Comments in Cache Not Found, Fetching ...")
            cache = _cached_fetch_video_comments(api_key, vid, comment_count)
        else:
            comm_n = cache["data"]["comm_n"]
            if comm_n < comment_count and refetch:
                print("[INFO]: Comments Not Enough In Cache %d < %d, Fetching ..." %(comm_n, comment_count))
                cache = _cached_fetch_video_comments(api_key, vid, comment_count)
            else:
                print("[INFO]: Not Fetching %d comments Of %s Is Available, to Force set refetch=True"%(comm_n, vid))
        file.close()
        return cache
    except FileNotFoundError as e:
            comm_n, comments = _cached_fetch_video_comments(api_key, vid, comment_count)
            cache = {}
            cache["labels"] = ["comments"]
            cache["data"] = {}
            cache["data"]["comments"] = comments
            cache["data"]["comm_n"] = comm_n
            return cache
    except Exception as e:
        print("[ERROR]: in cached_fetch_video_comments %s"%(e))
    return cache

def cached_fetch_video_info(api_key, vid, refetch=False):
    file_name = "../data/%s.json"%(vid)
    cache = None
    try:
        file = open(file_name, "r")
        file_data = file.read()
        cache = json.loads(file_data)
        valid_cache = False
        valid_cache = "ss_data" in cache["labels"]
        print("[INFO]: Found Cache ../data/%s.json "%(vid))
        if valid_cache == False:
            print("[INFO]: ss_data in Cache Not Found, Fetching ...")
            cache = _cached_fetch_video_info(api_key, vid)
        else:
            if refetch:
                print("[INFO]: Refetching SS_DATA ...")
                cache = _cached_fetch_video_info(api_key, vid)
            else:
                print("[INFO]: Not Fetching ss_data Is Available, to Force set refetch=True")
        file.close()
        return cache
    except FileNotFoundError as e:
            cache = _cached_fetch_video_info(api_key, vid)
            cache["labels"] = ["ss_data"]
            cache["data"]["ss_data"] = ss_data 
            return cache
    except Exception as e:
        print("[ERROR]: in cached_fetch_video_info %s"%(e))
    return cache
vid=""
cmn=0
try:
    vid = sys.argv[1]
    cmn = 30
    if len(sys.argv) > 2: cmn = int(sys.argv[2])

    cache = cached_fetch_video_comments(api_key, vid, cmn, True)
    data = cached_fetch_video_info(api_key, vid)
except Exception as e:
    print("[ERROR]: %s, %d | %s"%(vid, cmn, e) )
