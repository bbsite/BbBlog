from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from BeautifulSoup import BeautifulSoup

class BlogStatus:
    is_draft = 0
    is_ready_for_edit = 1
    is_edited = 2
    is_ready_for_final_review = 3
    is_published = 4

class BlogEntry(models.Model):
    title = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(unique_for_date='pub_date', blank=False)
    author = models.ForeignKey(User, related_name='author')
    pub_date = models.DateTimeField('date published', null=True)
    last_edit_date = models.DateField('date edited', null=True)
    editor = models.ForeignKey(User, null=True, related_name='editor')
    editable_content = models.TextField(blank=False)
    content = models.TextField(blank=False)
    tags = TaggableManager()
    PUB_STATUS = (
                  (BlogStatus.is_draft, 'Draft'),
                  (BlogStatus.is_ready_for_edit, 'Ready For Edit'),
                  (BlogStatus.is_edited, 'Has Been Edited'),
                  (BlogStatus.is_ready_for_final_review, 'Ready For Final Review'),
                  (BlogStatus.is_published, 'Published'),
                  )
    status = models.IntegerField(choices=PUB_STATUS, default=BlogStatus.is_draft)
    comments_enabled = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'blog entry'
        verbose_name_plural = 'blog entries'
    
    def __unicode__(self):
        return u'%s' % self.title
    
    def _highlight_python_code(self):        
        soup = BeautifulSoup(self.editable_content)
        python_code = soup.findAll("code", "python")
        
        lexer = get_lexer_by_name("python", stripall=True)
        formatter = HtmlFormatter()
        
        for code in python_code:
            code.replaceWith(highlight(code.string, lexer, formatter))         
            
        return str(soup)
    
    def save(self):
        self.content = self._highlight_python_code()
        super(BlogEntry, self).save()