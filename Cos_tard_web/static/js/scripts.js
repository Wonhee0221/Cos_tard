/*!
* Start Bootstrap - Modern Business v5.0.7 (https://startbootstrap.com/template-overviews/modern-business)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-modern-business/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project


// 페이지 상단으로 이동하는 버튼 로직
$(function() {
    $(window).scroll(function() {
        if ($(this).scrollTop() > 540) {
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

// 메인 페이지 접속할 때 버튼도 서서히 뜨게 하는 로직
document.addEventListener("DOMContentLoaded", function() {
    const fadingButton = document.getElementById("fading-button");
    setTimeout(() => {
      fadingButton.classList.add("visible-btn");
    }, 100); // Adding a slight delay to ensure smooth transition
  });
  