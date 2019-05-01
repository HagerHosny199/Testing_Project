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
#dina


    def test_play_list (self):
        #Decision Coverage criteria
        
        ydl=YoutubeDL.YoutubeDL()
        params = {'prefer_insecure' : False}
        downloader = downCommon.FileDownloader(ydl,params)
        extractor = extCommon.InfoExtractor(downloader = downloader)
        
        url = ['https://www.youtube.com/watch?v=H37yuTXXwo8', 'https://www.youtube.com/watch?v=nmZcGPIrojI', 'https://www.youtube.com/watch?v=T7kFMRhz0Tw']
      
        play_list = extractor.playlist_result(url , None , None , None)
        video_info = {'_type': 'playlist',
                      'entries': url,
                      }        
        self.assertEqual(play_list ,video_info )

        
        play_list = extractor.playlist_result(url , 1 , None , None)
        video_info = {'_type': 'playlist',
                      'entries': url,
                      'id' : 1,
                      }        
        self.assertEqual(play_list ,video_info ) 

        
        play_list = extractor.playlist_result(url , None , 'd7e7' , None)
        video_info = {'_type': 'playlist',
                      'entries': url,
                      'title' :'d7e7',
                      }
        
        self.assertEqual(play_list ,video_info ) 


        play_list = extractor.playlist_result(url , None , None , 'A channel that shows some of funny videos')
        video_info = {'_type': 'playlist',
                      'entries': url,
                      'description' :'A channel that shows some of funny videos',
                      }        
        self.assertEqual(play_list ,video_info )     

if __name__ == '__main__':
    unittest.main()
