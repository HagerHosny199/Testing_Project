from __future__ import unicode_literals

# Allow direct execution
import os
import sys
import unittest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import YoutubeDL

TEST_URL = 'https://www.youtube.com/watch?v=Wch3gJG2GJ4'
FAKE_URL='https://www.youtube.com/123'

def _make_result(formats, **kwargs):
    res = {
        'formats': formats,
        'id': 'testid',
        'title': 'testttitle',
        'extractor': 'testex',
        'extractor_key': 'TestEx',
        '_type': 'url',
        'url':TEST_URL,
        'webpage_url':TEST_URL,
        'webpage_url_basename':None,

    }
    res.update(**kwargs)
    return res

class TestYoutubeDL(unittest.TestCase):

    def test_trouble(self):
        """
        Here we test trouble function
        """
        ydl=YoutubeDL.YoutubeDL()
        message="Error has been occurred. "
        ydl.params['ignoreerrors']=False
        with self.assertRaises(Exception):
            ydl.trouble(message)

    def test_get_info_extractor(self):
        """
        Here we test get_info_extractor function
        I will apply statement coverage
        """
        ydl=YoutubeDL.YoutubeDL()
        ie_key='Youtube'
        ie=ydl.get_info_extractor(ie_key)
        self.assertNotEqual(ie,None)

    def test_process_info(self):
        """
            Here we test process_ie_result function
            I applied branch coverage criteria
        """
        # the first branch, if we use extract_flat & url we will get the same ie_result
        ydl=YoutubeDL.YoutubeDL()
        ydl.params['prefer_free_formats'] = True
        ydl.params['extract_flat']=True
        ydl.params['forcejson']=True
        formats = [
            {'ext': 'mp4', 'height': 460, 'url': TEST_URL},
        ]
        info_dict = _make_result(formats)
        results=ydl.process_ie_result(info_dict)
        self.assertEqual(results,info_dict)

        # the second branch, having the result_type == 'video'
        info_dict['_type']='video'
        results=ydl.process_ie_result(info_dict)
        print("results 2 =",results)
        self.assertEqual(results['ext'], 'mp4')

        # the third branch, result_type == 'url'
        ydl.params['extract_flat']=False
        info_dict['_type']='url'
        results=ydl.process_ie_result(info_dict)
        print("results 3 =",results)
        self.assertNotEqual(results,info_dict)

        # the 4th branch, result_type == 'url_transparent'
        info_dict = _make_result(formats)
        ydl.params['extract_flat']=False
        info_dict['_type']='url_transparent'
        print("sent data",info_dict)
        results=ydl.process_ie_result(info_dict)
        print("results 4 =",results)
        self.assertNotEqual(results,info_dict)

        # the 5th branch, result_type == 'playlist'
        info_dict = _make_result(formats)
        info_dict['_type']='playlist'
        info_dict['entries']=[]
        ydl.params['playliststart']=0
        ydl.params['playlistend']=1
        results=ydl.process_ie_result(info_dict)
        print("results 5 =",results)
        self.assertEqual(results['num_entries'],len(info_dict['entries']))

        # the 6th branch, result_type == 'compat_list'
        info_dict = _make_result(formats)
        info_dict['entries']=[]
        info_dict['_type']='compat_list'
        results=ydl.process_ie_result(info_dict)
        print("results 6 =",results)
        self.assertEqual(results['webpage_url_basename'],info_dict['webpage_url_basename'])

        # the 7th branch, result_type == UNKNOWN
        info_dict = _make_result(formats)
        info_dict['entries']=[]
        info_dict['_type']='UNKNOWN'
        with self.assertRaises(Exception):
            results=ydl.process_ie_result(info_dict)

    # Omar
    def test_format_resolution(self):
        """
        Here we test format_resolution function
        I will apply branch coverage
        """
        ydl = YoutubeDL.YoutubeDL()
        # branch1 'vcodec' == 'none'
        format = {"vcodec": "none"}
        result = ydl.format_resolution(format)
        self.assertEqual(result, 'audio only')
        # branch2 'resolution' != None
        format = {"resolution": 900}
        result = ydl.format_resolution(format)
        output = format['resolution']
        self.assertEqual(result, output)
        # branch3 'resolution' == None and height != None and width != None
        format = {"resolution": None, "height": 100, "width": 200}
        result = ydl.format_resolution(format)
        output = '%sx%s' % (format['width'], format['height'])
        self.assertEqual(result, output)
        # branch4 'resolution' == None and height != None and width == None
        format = {"resolution": None, "height": 100, "width": None}
        result = ydl.format_resolution(format)
        output = '%sp' % format['height']
        self.assertEqual(result, output)
        # branch5 'resolution' == None and height == None and width != None
        format = {"resolution": None, "height": None, "width": 100}
        result = ydl.format_resolution(format)
        output = '%dx?' % format['width']
        self.assertEqual(result, output)
        # branch6 'resolution' == None and height == None and width == None
        format = {"resolution": None, "height": None, "width": None}
        result = ydl.format_resolution(format)
        output = 'unknown'
        self.assertEqual(result, output)




if __name__ == '__main__':
    unittest.main()
