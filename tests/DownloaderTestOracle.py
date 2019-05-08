from __future__ import unicode_literals
import unittest
import os
import sys
import time
import random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from downloader import common
import YoutubeDL
class DownloaderTestOracle(unittest.TestCase):
    def test_format_seconds(self):
        """ This function takes seconds and produces the h:m:s format """
        ydl=YoutubeDL.YoutubeDL()
        downloader=common.FileDownloader(ydl,None)
        # generate random number
        seconds=random.randint(3700,10000)
        # get the function output
        results=downloader.format_seconds(seconds)
        # calculate the right output
        secs=seconds%60
        mins=seconds/60
        hours=mins/60
        mins=mins%60
        output='%02d:%02d:%02d' % (hours, mins, secs)
        # check if they are equal
        self.assertEqual(results,output)

    def test_format_percent(self):
        ydl=YoutubeDL.YoutubeDL()
        downloader=common.FileDownloader(ydl,None)
         # generate random number
        percent=random.uniform(0,100)
        results = downloader.format_percent(percent)
        output = str(round(percent, 1)) + '%'
        while(len(output) < 6):
            output = " " + output
         # check if they are equal
        self.assertEqual(results,output)
    
    def test_best_block_size(self):
        """ This function takes elapsed time and bytes and produces value between 1 & 4194304 """
        ydl=YoutubeDL.YoutubeDL()
        downloader=common.FileDownloader(ydl,None)
        bytes=random.randint(1,1000)
        elapsed_time=random.randint(0,120)
        rate = bytes / elapsed_time
        # get the output
        output=downloader.best_block_size(elapsed_time, bytes)
        # check that the output in this interval [1,4194304]
        self.assertGreaterEqual(output,1)
        self.assertLessEqual(output,4194304)
        # check that we got the right output
        if elapsed_time<0.001 :
            self.assertEqual(output,int(min(max(bytes * 2.0, 1.0), 4194304)))
        #check the rate cases
        elif rate > min(max(bytes * 2.0, 1.0), 4194304):
            self.assertEqual(output,int(min(max(bytes * 2.0, 1.0), 4194304)))
        elif rate < max(bytes / 2.0, 1.0):
            self.assertEqual(output,int(max(bytes / 2.0, 1.0)))
        else:
            self.assertEqual(output,int(rate))

if __name__ == '__main__':
    unittest.main()
