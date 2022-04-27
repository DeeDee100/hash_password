from django.contrib import admin
from core.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","slug", "author", "published", "status")
    list_filter = ("status", "data_creation", "published", "author")
    raw_id_fields = ("usuario",)
    data_hierarchy = "publicado"
    search_fields = ("title", 'conteudo')
    prepopulated_fields = {'slug':('title',)}
    
"""
     title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    author = models.CharField(max_length=50)
    text = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    data_creation = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, 
                                on_delete=models.CASCADE)
    up_image = models.ImageField(blank=True, null=True)
    status = models.CharField(max_length=10, 
                              choices=STATUS, 
                              default='rascunho')
    
"""