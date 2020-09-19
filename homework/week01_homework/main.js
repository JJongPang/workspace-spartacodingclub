"use strict";

const orderBtn = document.querySelector(".order__btn");

orderBtn.addEventListener("click", checkMessage);

function checkMessage() {
  const orderName = document.getElementById("order-name");
  const orderSelect = document.querySelector(".select__box");
  const orderAddress = document.getElementById("order-address");
  const orderTel = document.getElementById("order-tel");

  if (orderName.value === "") {
    alert("주문자 이름을 입력해주세요");
  } else if (orderSelect.value === "수량선택") {
    alert("수량을 입력해주세요.");
  } else if (orderAddress.value === "") {
    alert("주소를 입력해주세요.");
  } else if (orderTel.value === "") {
    alert("전화번호를 입력해주세요.");
  } else {
    alert(
      `주문자이름: ${orderName.value}\n수량: ${orderSelect.value}\n주소: ${orderAddress.value}\n전화번호: ${orderTel.value}`
    );
  }
}
