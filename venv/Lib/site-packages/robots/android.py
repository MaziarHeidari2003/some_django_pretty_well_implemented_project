# -*- coding: utf-8 -*-
# @author: leesoar

"""Android Bot"""

import functools
import random
import subprocess
import time

from lxml import etree

__all__ = ["AndroidBot"]


def run_check(func):
    @functools.wraps(func)
    def wrapper(cls, *args, **kwargs):
        ret = func(cls, *args, **kwargs)
        if cls._raise_error and ret and ((ret.stdout and ret.stdout.startswith(b"Error")) or ret.returncode != 0):
            raise cls.RobotRunError("Is the device still online?")
        return ret
    return wrapper


class AndroidBot:
    RobotRunError = type("RobotRunError", (Exception,), {})

    def __init__(self, serial=None, raise_run_error=True):
        self.__adb_path = "adb"
        self.serial = serial
        self._raise_error = raise_run_error

    @run_check
    def __run(self, *args, use_serial=True, **kwargs):
        try:
            if use_serial:
                return subprocess.run(map(str, self.__exec_with_serial() + args[0]), capture_output=True, **kwargs)
            return subprocess.run(*args, capture_output=True, **kwargs)
        except FileNotFoundError:
            print("\033[1;31;m[Warning]: adb not found, you need to set the path first.\033[0m")

    def set_adb_path(self, path):
        self.__adb_path = path
        self.connect()

    def connect(self, serial=None):
        self.serial = self.serial or serial
        return self.__run([self.__adb_path, "connect", self.serial], use_serial=False)

    def __exec_with_serial(self):
        return [self.__adb_path] + (["-s", self.serial] if self.serial else [])

    def open(self, url_scheme):
        return self.__run(["shell", "am", "start", "-a", "android.intent.action.VIEW", "-d", url_scheme])

    def press_key(self, code):
        return self.__run(["shell", "input", "keyevent", code])

    def back(self):
        return self.press_key(4)

    def tap(self, x, y):
        return self.__run(["shell", "input", "tap", x, y])

    def input(self, text):
        return self.__run(["shell", "input", "text", text])

    def screen_size(self) -> list:
        res = self.__run(["shell", "wm", "size"])
        return res and list(map(int, res.stdout.decode().strip().rsplit(" ")[-1].split("x")))

    def xpath(self, p):
        xml = self.xml()
        if not xml:
            return
        node = etree.XML(xml)
        return node.xpath(p)

    def xml(self) -> bytes:
        res = subprocess.run(
            f'{self.__adb_path} {" -s " + self.serial if self.serial else ""} exec-out "uiautomator dump | xargs cat 2>/dev/null"',
            shell=True, capture_output=True)

        if res and res.stdout.startswith(b"Killed"):
            return
        return res and res.stdout

    @staticmethod
    def delay(*rg, max_=60):
        if not rg:
            rg = (3, 5)
        if len(rg) == 1:
            time.sleep(*rg)
        else:
            time.sleep(min(random.uniform(*rg), max_))

    @staticmethod
    def __random(digit, threshold):
        return random.randint(digit - threshold, digit + threshold)

    def swipe(self, x1, y1, x2, y2, speed=200, threshold=25):
        self.__run([
            "shell", "input", "swipe",
            self.__random(x1, threshold),
            self.__random(y1, threshold),
            self.__random(x2, threshold),
            self.__random(y2, threshold),
            speed,
        ])
