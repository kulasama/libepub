libepub
======================= 


example:
--------
  
    >>> from libepub import EPub
    >>> epubfile = '../tests/犹太商人羊皮卷.epub'
    >>> epub = EPub(epubfile)
    >>> title = epub.title()      
    >>> author = epub.author()
    >>> chapters = epub.chapters() 
    >>> chapter = chapters[0]  
    >>> content = epub.read_content(chapter['id'])   




