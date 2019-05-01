import unittest
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
        output = '%10s' % ('%s/s' % format_bytes(speed))
        self.assertEqual(results, output)




if __name__ == '__main__':
    unittest.main()

