// const text="\"까불지마, 1등은 우리꺼야.\"";
// var count=0;
// function showText() {
//     count++;
//     var typing = document.getElementById("typing-effect");
//     if (count > text.length) {
//         typing.innerText="까";
//         count=1;
//     } else {
//         typing.innerText=text.substr(0,count);
//     }
//     setTimeout(showText, 200);
// }
// // 페이지 로드 시 타이핑 효과를 적용하도록 호출
// window.onload = showText;



const introText = document.querySelectorAll("span");

window.onload = () => {
  let timer = 100;
  introText.forEach((item) => {
    item.style.animation = `fade 500ms ${(timer += 70)}ms forwards`;
  });
};