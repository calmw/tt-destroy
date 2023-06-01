import json
import logging
import os

currPath = os.path.dirname(os.path.abspath(__file__))


def get_poll_height():
    pool_height_file = "{}/poll_height.json".format(currPath)
    try:
        with open(pool_height_file) as f:
            pool_height = json.load(f)
            return pool_height["height"]
    except Exception as e:
        logging.error("get_poll_height error:", e)
        return None


def save_poll_height(height):
    pool_height_file = "{}/poll_height.json".format(currPath)
    try:
        with open(pool_height_file, "w") as f:
            json.dump({"height": height}, f)
    except Exception as e:
        logging.error("save_poll_height error:", e)
        return None
