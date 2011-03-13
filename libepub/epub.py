#coding:utf8
import unittest     
import zipfile
from BeautifulSoup import BeautifulStoneSoup

class EPub(object) :
    
    def __init__(self,path):
        o = zipfile.ZipFile(path, mode='r') 
        buf = o.read('toc.ncx')      
        self.soap = BeautifulStoneSoup(buf, fromEncoding='utf8')  
        
    def title(self):  
        return unicode(self.soap.ncx.doctitle.text.string)     
        
    def author(self):
        return unicode(self.soap.ncx.docauthor.text.string)
    
        

    
                   
                     
        
class EPubTestCase(unittest.TestCase):
    
    def test_read(self): 
        epubfile = '../tests/犹太商人羊皮卷.epub'
        epub = EPub(epubfile)
        title = epub.title()      
        self.assertEqual(title,u'犹太商人羊皮卷')  
        author = epub.author()
        self.assertEqual(author,u'弥赛亚')
        
        
        

if __name__ == '__main__':
    unittest.main()
       
        
        

