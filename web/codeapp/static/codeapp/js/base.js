/**
 * Created by rene on 23/7/17.
 */
$(document).ready(function () {
    console.log("Loading js");
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });

});