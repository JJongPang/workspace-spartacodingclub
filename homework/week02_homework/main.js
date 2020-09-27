"use strict";

exchangeRage();

function checkMessage() {
  const orderName = $("#order-name");
  const orderSelect = $(".select__box");
  const orderAddress = $("#order-address");
  const orderTel = $("#order-tel");

  var regPhone = /(01[0|1|6|9|7])[-](\d{3}|\d{4})[-](\d{4}$)/g;

  if (orderName.val() === "") {
    alert("주문자 이름을 입력해주세요");
  } else if (orderSelect.val() === "수량선택") {
    alert("수량을 입력해주세요.");
  } else if (orderAddress.val() === "") {
    alert("주소를 입력해주세요.");
  } else if (orderTel.val() === "") {
    alert("전화 번호를 입력해주세요");
  } else if (!regPhone.test(orderTel.val())) {
    alert("올바른 전화 번호를 입력해주세요. ex) 000-0000-0000");
  } else {
    alert(
      `주문자이름: ${orderName.val()}\n수량: ${orderSelect.val()}\n주소: ${orderAddress.val()}\n전화번호: ${orderTel.val()}`
    );
  }
}

function exchangeRage() {
  const rate = $(".exchange__rage");

  const getExchangeRage = () => {
    try {
      return axios.get("https://api.manana.kr/exchange/rate.json");
    } catch (error) {
      console.error(error);
    }
  };

  const exchangeRangeData = async () => {
    const check = await getExchangeRage();

    const checkValue = check.data[1]["rate"];

    const inputHtml = `<strong class="rate">달러-원 환율 : ${checkValue}</strong>`;

    rate.append(inputHtml);
  };
  exchangeRangeData();
}
