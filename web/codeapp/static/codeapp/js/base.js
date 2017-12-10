/**
 * Created by rene on 23/7/17.
 */
$(document).ready(function () {
    console.log("Loading js");
    $(document).ready(function () {
        $('.dropdown-toggle').dropdown();
        $('#sidebarCollapse').on('click', function () {
            $('#sidebar').toggleClass('active');
        });

        // To style all <select>s
        $('select').selectpicker();
    });

});