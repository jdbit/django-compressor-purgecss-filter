# Remove unused CSS classes with the PurgeCSS filter for Django Compressor
PurgeCSS filter for Django Compressor removes unused CSS and makes your CSS files smaller. It automatically discovers all your template files and scans them for CSS classes then removes unused classes from your CSS files. Django Compressor also merges and minimizes your CSS files.

## Usage

1. Install [Django Compressor](https://django-compressor.readthedocs.io/en/stable/quickstart.html#installation), add `'compressor'` to your `INSTALLED_APPS`.
2. Add your styles inside Django compressor tags just like this:
```
{% load compress %}
{% compress css %}
    <link href="/static/scss/bootstrap.css" rel="stylesheet" type="text/css">
    <link href="/static/css/styles.css" rel="stylesheet" type="text/css">
    <link href="/static/css/fontello.css" rel="stylesheet" type="text/css">
    <link href="/static/css/some_other_styles.css" rel="stylesheet" type="text/css">
{% endcompress %}
```
3. Install [PurgeCSS](https://purgecss.com/getting-started.html) and make `purgecss` CLI command available globally with this command: `npm i -g purgecss`
4. Copy `purgecss_filter.py` file to your Django app, for example, to an app folder.
5. Add the filter to the Django Compressor filter setting in `settings.py`:
```
COMPRESS_FILTERS = {'css': ['YOUR_APP_NAME.purgecss_filter.PurgeCSSFilter', 'compressor.filters.css_default.CssAbsoluteFilter', 'compressor.filters.cssmin.rCSSMinFilter'], 'js': ['compressor.filters.jsmin.rJSMinFilter']}
```
6. *(optional)* Turn on CSS compression when `DEBUG = True` by adding `COMPRESS_ENABLED = True` to `settings.py`.

## If you would like to use it with SCSS files

Install and configure [django-libsass](https://github.com/torchbox/django-libsass).

## If the filter removes some classes that are actually in use

This may happen when you have some dynamically loaded classes from JS, Python code, or when you use some classes in your content that don't exist in templates. You can fix this by adding an argument to PurgeCSS to whitelist CSS classes that should not be removed:
```
COMPRESS_PURGECSS_ARGS = "--safelist Class-name1 Class-name2 Class-name3"
```
By default, the filter doesn't scan third-party installed apps for templates, but you can include these templates as well with this setting:
```
COMPRESS_PURGECSS_APPS_INCLUDED [
    'allauth',
    'crispy',
    ...
]
```
