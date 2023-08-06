/*!
* Start Bootstrap - Modern Business v5.0.7 (https://startbootstrap.com/template-overviews/modern-business)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-modern-business/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project


$(function() {
    $(window).scroll(function() {
        if ($(this).scrollTop() > 540) { //560.12
            $('.move_to_top_btn').fadeIn();
        } else {
            $('.move_to_top_btn').fadeOut();
        }
    });

    $('.move_to_top_btn').click(function() {
        $('html, body').animate({
            scrollTop: 0
        }, 100);
        return false;
    });
});
