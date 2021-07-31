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

## Configure CKEditor in Settings
- [ ]  Add the following setting in `settings.py`
```py
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Add path file uploads 
CKEDITOR_UPLOAD_PATH = "uploads/"

# Configure CKEditor
CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'icy_orange',
        'toolbar': 'Habib',
        'toolbar_Habib': [
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl']},
            {'name': 'editing', 'items': [
                'Find', 'Replace']},
            {'name': 'yourcustomtools', 'items': ['Preview', 'Maximize']},
            '/',  # End of first line of CKEditor
            {'name': 'styles', 'items': [
                'Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',  # End of second line of CKEditor
            {'name': 'mydev', 'items': [
                'Youtube', 'CodeSnippet', 'ExportPdf', 'Uploadfile', 'Mathjax']},
            # put this to force next toolbar on new line

        ],
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'fontSize_defaultLabel': 44,
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage',  # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
            'link', ' iframe', 'colorbutton', 'youtube',
            'codesnippet',
            'exportpdf',
            'uploadfile',
            'mathjax',

        ]),
    }
}
```

## Add custom plugins or CKEDITOR skins 

- [ ] Go to [ CKEDITOR Plugin](https://ckeditor.com/cke4/addons/plugins/all) official site
- [x] Download which plugins or skin you need 
- [x] Extract plugin or skin you downloaded. Copy inside plugin or skin folder
- [x] Paste plugin in your project env directory  `...\env\Lib\site-packages\ckeditor\static\ckeditor\ckeditor\plugins`
- [x] Paste skin in your project env directory  `...\env\Lib\site-packages\ckeditor\static\ckeditor\ckeditor\skins`

## Collect statistic to gather all under the same roof
```py
python manage.py collectstatistic
```

### That's all about it. Keep coding...
**Thank you for keeping patience.**
**_If you love it do mark the [Repository](https://github.com/mhhabib/Integrate-Django-Ckeditor) as **stars** or **forks**_**

