$(document).ready(function () {
    var textarea = $('#id_text');
    textarea.css({display: 'none'});
    var editor = ace.edit("editor");
    editor.setTheme("ace/theme/chrome");
    editor.getSession().setMode("ace/mode/text");
    $("#id_language").change(function () {
        editor.getSession().setMode("ace/mode/" + $(this).val());
    });

    editor.getSession().on('change', function () {
        textarea.val(editor.getSession().getValue());
    });
    editor.setValue(textarea.val());
});