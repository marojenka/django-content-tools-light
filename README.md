Django contenttools.js integration
----------------------------------

Simplified example integration of amazing
[contenttools](http://getcontenttools.com) into Django project.  The aim was to
adopt contenttools in a WYSIWYG-editor manner with minimal changes to existing
projects.  It's simplified so that data is send via synchronous POST request.

This is for personal use, for proper integration one should use approach
made in [django-contenttools-demo](https://github.com/Cotidia/django-contenttools-demo).

## Core
contenttools is a lovely customisable editor that allows you to easily generate
content with hmtl-markup. Such an instrument is a perfect replacement for bunch
of rich text editors loaded in django-admin interface without styles and
context of a page.

In this simplest example pages are generated via `Page` model with `content` `TextField`.
Contenttools is used to populate this field via synchronous POST request.

Everything that is (hardly) worth looking at are:

```
base/static/editor.js
pages/views.py
pages/templates/pages/page_form.html
```

## Hack
In order to use contenttools not only for saving HTML markup but for editing
embeded distict fields that should not be evaluated as HTML data little hack is
suggested.  One might wrap model field with desired html tag, h1 or p or any
div, by contenttools and then in backend strip this tag keeping data and markup
separated.

## See also
+ Core project [contenttools](http://getcontenttools.com)
+ Correct integration with django [django-contenttools-demo](https://github.com/Cotidia/django-contenttools-demo)

## License
MIT license
