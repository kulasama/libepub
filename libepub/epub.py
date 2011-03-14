#coding:utf8
import unittest     
import zipfile
from BeautifulSoup import BeautifulStoneSoup,BeautifulSoup

class EPub(object) :
    
    def __init__(self,path):
        self.o = zipfile.ZipFile(path, mode='r') 
        buf = self.o.read('toc.ncx')      
        self.soap = BeautifulStoneSoup(buf, fromEncoding='utf8')  
        
    def title(self):  
        return unicode(self.soap.ncx.doctitle.text.string)     
        
    def author(self):
        return unicode(self.soap.ncx.docauthor.text.string)  
        
    def chapters(self):
        chapters = self.soap.findAll('navpoint',{'class':'chapter'})    
        return chapters
        
    def get_chapter_content(self,chapter_id):
        fname = '%s.html' % chapter_id
        buf = self.o.read(fname) 
        buf_soap = BeautifulSoup(buf,fromEncoding='utf8') 
        body = buf_soap.html.body.decodeContents('utf8')
        return body
            
    
        
    
        

    
                   
                     
        
class EPubTestCase(unittest.TestCase):
    
    def test_read(self): 
        epubfile = '../tests/犹太商人羊皮卷.epub'
        epub = EPub(epubfile)
        title = epub.title()      
        self.assertEqual(title,u'犹太商人羊皮卷')  
        author = epub.author()
        self.assertEqual(author,u'弥赛亚')   
        chapters = epub.chapters() 
        chapter = chapters[0]  
        content = epub.get_chapter_content(chapter['id'])  

        
        

if __name__ == '__main__':
    unittest.main()
       
        
        

