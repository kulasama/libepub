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
        navpoints = self.soap.findAll('navpoint',{'class':'chapter'})   
        chapters = []
        for point in navpoints: 
            chapter = {}
            chapter['id'] = point['id']
            chapter['class'] = point['class']
            chapter['playorder'] = point['playorder']
            chapter['label'] = unicode(point.navlabel.text.string)
            chapters.append(chapter)
            
        return chapters
        
    def read_content(self,chapter_id):
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
        self.assertEqual(chapter,{'label': u'Chapter_1', 'playorder': u'1', 'id': u'article_102774_1', 'class': u'chapter'})
        content = epub.read_content(chapter['id'])   
        print content
      

        
        

if __name__ == '__main__':
    unittest.main()
       
        
        

