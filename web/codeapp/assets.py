from django_assets import Bundle, register

js = Bundle('static/codeapp/libs/js/jquery.min.js',
            'static/codeapp/libs/js/bootstrap.min.js',
            filters='jsmin', output='static/codeapp/gen/packed.js')
register('js_all', js)

js = Bundle('static/codeapp/js/base.js',
            filters='jsmin', output='static/codeapp/gen/packed2.js')
register('js_all2', js)
#
css = Bundle(
    # 'static/css/base.scss',
    'static/codeapp/libs/css/bootstrap.min.css',
    output='static/codeapp/gen/packed.css')
register('css_all', css)

css_custom = Bundle(
    'static/codeapp/css/base.scss',
    filters='pyscss, cssmin', output='static/codeapp/gen/packed2.css')
register('css_all2', css_custom)
