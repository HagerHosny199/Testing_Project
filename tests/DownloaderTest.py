from __future__ import unicode_literals
import unittest
import os
import sys
import time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from downloader import common
import YoutubeDL
class DownloaderTest(unittest.TestCase):
    def test_format_seconds(self):
        """
        Here we test downloader/common/format_seconds function
        We will apply predicate coverage criteria
        """
        ydl=YoutubeDL.YoutubeDL()
        downloader=common.FileDownloader(ydl,None)

        # predicate(hours>99) is True
        seconds=100*60*60
        results=downloader.format_seconds(seconds)
        self.assertEqual(results,'--:--:--')

        # predicate(hours>99) is False & predicate (hours==0) is True
        seconds=60
        secs=seconds%60
        mins=seconds/60
        output='%02d:%02d' % (mins, secs)
        results=downloader.format_seconds(seconds)
        self.assertEqual(results,output)

        # predicate(hours==0) is False
        seconds=10*60*60
        secs=seconds%60
        mins=seconds/60
        hours=mins/60
        mins=mins%60
        output='%02d:%02d:%02d' % (hours, mins, secs)
        results=downloader.format_seconds(seconds)
        self.assertEqual(results,output)

    def test_slow_down(self):
        """
        Here we test downloader/common/slow_down function
        We will apply clause coverage criteria
        """
        start_time=10
        now=12
        byte_counter=10
        ydl=YoutubeDL.YoutubeDL()
        # evaluate clause (rate_limit is None) to True & clause (byte_counter==0) to False
        ydl.params['ratelimit']=None
        downloader=common.FileDownloader(ydl,ydl.params)


    # Omar
    def test_calc_percent(self):
        """Here we test downloader/common/calc_percent function
         We will apply predicate coverage criteria"""
        ydl = YoutubeDL.YoutubeDL()
        downloader = common.FileDownloader(ydl, None)
        # data_len is None = True
        data_len = None
        byte_counter = 200
        results = downloader.calc_percent(byte_counter, data_len)
        self.assertEqual(results, None)
        # data_len is None = False
        data_len = 100
        output = float(byte_counter) / float(data_len) * 100.0
        results = downloader.calc_percent(byte_counter, data_len)
        self.assertEqual(results, output)

    def test_format_percent(self):
        """Here we test downloader/common/format_percent function
         We will apply predicate coverage criteria"""
        ydl = YoutubeDL.YoutubeDL()
        downloader = common.FileDownloader(ydl, None)
        # percent is None = True
        percent = None
        results = downloader.format_percent(percent)
        self.assertEqual(results, '---.-%')
        # percent is None = False
        percent = 13
        output = '%6s' % ('%3.1f%%' % percent)
        results = downloader.format_percent(percent)
        self.assertEqual(results, output)

    def test_calc_speed(self):
        """Here we test downloader/common/calc_speed function
         We will apply Clause coverage criteria"""
        ydl = YoutubeDL.YoutubeDL()
        downloader = common.FileDownloader(ydl, None)
        #  (bytes == 0) True , (dif < 0.001) True
        bytes = 0
        now = 100
        start = 100
        results = downloader.calc_speed(start, now, bytes)
        self.assertEqual(results, None)
        #  (bytes == 0) False , (dif < 0.001) False
        bytes = 10
        now = 100
        start = 50
        results = downloader.calc_speed(start, now, bytes)
        output = float(bytes) / (now - start)
        self.assertEqual(results, output)

    def test_format_speed(self):
        """Here we test downloader/common/format_speed function
         We will apply predicate coverage criteria"""
        ydl = YoutubeDL.YoutubeDL()
        downloader = common.FileDownloader(ydl, None)
        # percent is None = True
        speed = None
        results = downloader.format_speed(speed)
        self.assertEqual(results, '%10s' % '---b/s')
        speed = 20
        results = downloader.format_speed(speed)
        
        output = '%10s' % ('%s/s' % common.format_bytes(speed))
        self.assertEqual(results, output)



    def test_calc_eta (self):
        #Condition Decision Coverage criteria
        ydl=YoutubeDL.YoutubeDL()
        downloader=common.FileDownloader(ydl,None)
        now = time.time()
        start = now - 100
        total = 1000
        current = 10

        eta = downloader.calc_eta(start,now,total,current)
        self.assertEqual(eta , 9900)

        eta = downloader.calc_eta(start,now,None,current)
        self.assertEqual(eta , None)
        
        eta = downloader.calc_eta(start,None,total,current)
        self.assertEqual(eta , 9900)        

        eta = downloader.calc_eta(start,now,total,0)
        self.assertEqual(eta , None) 
        
        start = now
        eta = downloader.calc_eta(start,now,total,current)
        self.assertEqual(eta , None)


    def test_best_block_size (self):
        #Decision Coverage criteria

        ydl=YoutubeDL.YoutubeDL()
        downloader=common.FileDownloader(ydl,None)
        elapsed_time = 1
        bytes_ = 20
        size  = downloader.best_block_size(elapsed_time, bytes_)
        self.assertEqual(size , 20)

        elapsed_time = 0.0001
        bytes_ = 20
        size  = downloader.best_block_size(elapsed_time, bytes_)
        self.assertEqual(size , 40) 

        elapsed_time = 0.1
        bytes_ = 20
        size  = downloader.best_block_size(elapsed_time, bytes_)
        self.assertEqual(size , 40)  
        
        elapsed_time = 4
        bytes_ = 20
        size  = downloader.best_block_size(elapsed_time, bytes_)
        self.assertEqual(size , 10)
    
    def test_format_eta(self):
        """Testing format_eta function"""
        """Applying branch coverage"""
        ydl=YoutubeDL.YoutubeDL()
        downloader=common.FileDownloader(ydl,None)
        
        """1st branch: eta = None"""
        eta = None
        result = downloader.format_eta(eta)
        self.assertEqual(result, '--:--')
        
        """2st branch: eta != None"""
        eta = 50
        result = downloader.format_eta(eta)
        self.assertEqual(result, '00:50')

if __name__ == '__main__':
    unittest.main()
