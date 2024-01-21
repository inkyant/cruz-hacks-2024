
from random import randint
from .api_keys import REPLICATE_API_KEY, CDN_CLOUD_NAME, CDN_API_KEY, CDN_API_SECRET

import replicate
import cloudinary.uploader
import os
import cv2
import asyncio
from functools import partial
import threading
import time

import cloudinary
          
cloudinary.config( 
  cloud_name = CDN_CLOUD_NAME, 
  api_key = CDN_API_KEY, 
  api_secret = CDN_API_SECRET
)

os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_KEY

# converts video into i frames
def extractImages(pathIn, i):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    frame_jump_amount = vidcap.get(cv2.CAP_PROP_FRAME_COUNT) / i
    success, image = vidcap.read()
    while success and count < i:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*frame_jump_amount))
        success, image = vidcap.read()
        if not success: break
        cv2.imwrite("./frame%d.jpg" % count, image)
        count = count + 1

def process_frame(i, rand_id, data):
    # upload to CDN
    public_id = str(rand_id) + "_frame" + str(i)
    cloudinary.uploader.upload("./frame%d.jpg" % i, public_id = public_id)
    print("Running")

    # AI Analysis
    output = replicate.run(
        "yorickvp/llava-13b:e272157381e2a3bf12df3a8edd1f38d1dbd736bbb7437277c8b34175f8fce358",
        input={
            "image": "https://res.cloudinary.com/" + CDN_CLOUD_NAME + "/image/upload/f_auto,q_auto/" + public_id,
            "prompt": "Describe what is occuring in this frame from a video." + data["context"]
        }
    )

    # for next analysis, include context
    if data["context"] == "":
        data["context"] = " Here are descriptions of the previous frames: \n"

    # The yorickvp/llava-13b model can stream output as it's running.
    # The predict method returns an iterator, and you can iterate over that output.
    output = ''.join(output)

    # add context, update description
    data["context"] += output + "\n"
    print("="*6)
    print(data["context"])
    print("="*6)
    data["final_description"] = output

    # delete images once we're done with them
    os.remove("./frame%d.jpg" % i)
    cloudinary.uploader.destroy(public_id)
    # Indicate that the thread is done running
    data["status"][i] = 1

async def video_caption(path):

    # convert video to images
    num_images = 3
    extractImages(path, num_images)

    # final_description = ""
    # context = ""

    data = {"final_description": "", "context": "", "status": [0 for _ in range(num_images)]}
    threads = []

    rand_id = randint(0, 999)
    for i in range(num_images):
        # process_frame(i, rand_id, data)
        threads.append(threading.Thread(target=process_frame, args=(i, rand_id, data)))
    
    for thread in threads:
        thread.start()
    
    # Wait until all threads are finished running
    while 0 in data["status"]:
        time.sleep(0.1)

    # return final_description
    return data["final_description"]


if __name__ == "__main__":
    
    video_caption("@queenchelsea_video_7322611233415531782.mp4")
