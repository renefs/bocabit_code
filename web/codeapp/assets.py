from django_assets import Bundle, register

js = Bundle('static/codeapp/libs/js/jquery.min.js',
            'static/codeapp/libs/js/bootstrap.min.js',
            filters='jsmin', output='static/codeapp/gen/packed.js')
register('js_libs', js)

js = Bundle('static/codeapp/js/base.js',
            filters='jsmin', output='static/codeapp/gen/packed2.js')
register('js_custom', js)
#
css = Bundle(
    # 'static/css/base.scss',
    'static/codeapp/libs/css/bootstrap.min.css',
    'static/codeapp/libs/css/bootstrap-social.css',
    'static/codeapp/libs/css/font-awesome.css',
    output='static/codeapp/gen/packed.css')
register('css_libs', css)

css_custom = Bundle(
    'static/codeapp/css/base.scss',
    filters='pyscss, cssmin', output='static/codeapp/gen/packed2.css')
register('css_custom', css_custom)
