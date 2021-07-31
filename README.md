# [Ckeditor](https://ckeditor.com/) Integration in Django model.

One of the popular Django richtext editor is CKEditor. It provides a `RichTextField`, `RichTextUploadingField`, `CKEditorWidget` and `CKEditorUploadingWidget` utilizing CKEditor
with image uploading and browsing support included.

## Steps to integrate CKEditor in Django
- [ ] Install django-ckeditor to your project path
  
    `pip install django-ckeditor`
- [ ] Add `ckeditor` to your `INSTALLED_APPS` in `settings.py`.
  
  ```py
  INSTALLED_APPS = [
    .........
    'ckeditor',
  ]
  ```
- [ ] Required for using widget with file upload
  
      Add `ckeditor_uploader` to your `INSTALLED_APPS ` setting
 
- [ ] Add a `CKEDITOR_UPLOAD_PATH` setting to the project’s `settings.py` file
  
      ```py
      CKEDITOR_UPLOAD_PATH = "uploads/"
      ```
- [ ] Add CKEditor URL include to your project’s `urls.py` file
    ```py
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    
    # You can also set url path alternatively if the above url doesn't work
    path('ckeditor/', include('ckeditor_uploader.urls')),
    ```
    
## Use CKEditor in Django model
- [ ] Go to `models.py` and create a class where you want to use `RichTextField` and `import RichTextField`
```py
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Posts(models.Model):
    title = models.CharField(max_length=200) # Set your own
    description = RichTextField()
    
    # If you need to upload file then use RichTextUploadingField
    description = RichTextUploadingField(blank=True, null=True)
```
