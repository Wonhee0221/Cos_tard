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

// 타이핑 효과로 h1태그 내용 보여주는 자바스크립트인데 적용이 안됨..

// var text="Cos-tard의 인스타그램 인플루언서 자동추천 시스템을 사용해보세요";
// var count=0;
// function showText() {
//     count++;
//     var typing = document.getElementById("typingEffect");
//     if (count > text.length) {
//         typing.innerText="";
//         count=0;
//     } else {
//         typing.innerText=text.substr(0,count);
//     }
//     setTimeout(showText, 150)
// }
