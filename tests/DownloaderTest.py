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




if __name__ == '__main__':
    unittest.main()

