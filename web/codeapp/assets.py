from django_assets import Bundle, register

js = Bundle('static/codeapp/libs/js/jquery.min.js',
            'static/codeapp/libs/js/semantic.min.js',
            'static/codeapp/libs/js/jquery.dataTables.min.js',
            'static/codeapp/libs/js/dataTables.semanticui.min.js',
            'static/codeapp/js/base.js',
            filters='jsmin', output='static/codeapp/gen/packed.js')
register('js_all', js)
#
css = Bundle(
    # 'static/css/base.scss',
    'static/codeapp/libs/css/semantic.min.css',
    'static/codeapp/libs/css/dataTables.semanticui.min.css',
    output='static/codeapp/gen/packed.css')
register('css_all', css)

css_custom = Bundle(
    'static/codeapp/css/base.scss',
    filters='pyscss, cssmin', output='static/codeapp/gen/packed2.css')
register('css_all2', css_custom)