import unittest
from extractor import common as extCommon
from downloader import common as downCommon
import YoutubeDL

class ExtractorTest(unittest.TestCase):
    def test__proto_relative_url(self):
        """
        Testinf extractor/common/_proto_relative_url function
        Applying branch coverage
        """
        ydl=YoutubeDL.YoutubeDL()
        params = {'prefer_insecure' : False}
        
        downloader = downCommon.FileDownloader(ydl,params)
        extractor = extCommon.InfoExtractor(downloader = downloader)
        
        """First branch: url = None, scheme = None"""
        url = None
        result = extractor._proto_relative_url(url = url)
        self.assertEqual(result, url)
        
        """second branch: url.startswith('//') = True, scheme = None"""
        downloader.params['prefer_insecure'] = False #to make  scheme = 'https:'
        extractor.set_downloader(downloader)
        url = '//example.com/'
        result = extractor._proto_relative_url(url)
        self.assertEqual(result, 'https:' + url)
        
        """third branch: url.startswith('//') = True, scheme = 'https'"""
        extractor._downloader.params['prefer_insecure'] = False #scheme = 'http:'
        url = '//example.com/'
        result = extractor._proto_relative_url(url, 'https:')
        self.assertEqual(result, 'https:' + url)
        
        """fourth branch: url.startswith('//') = False"""
        url = 'https//example.com/'
        result = extractor._proto_relative_url(url, 'https')
        self.assertEqual(result, url)

if __name__ == '__main__':
    unittest.main()