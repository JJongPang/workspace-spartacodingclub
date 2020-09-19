'use strict'

const makeBtn = document.querySelector('.btn-save');

// button event
makeBtn.addEventListener('click', warningMessage);

// warning message function
function warningMessage() {
    const formUrl = document.querySelector('.form-url');
    const formComment = document.querySelector('.form-comment');
    
    if(formUrl.value === '' && formComment.value === '') {
        alert('아티클URL, 간단코멘트 입력해주세요.');
    }else if(formUrl.value === "") {
        alert('아티클URL이 입력이 안됬습니다.');
    }else if(formComment.value === "") {
        alert('간단코멘트가 입력이 안됬습니다.');
    }else {
        alert(`아티클URL: ${formUrl.value}\n간단코멘트: ${formComment.value}`);
    }
}