// Открытие пака 	

let pack = document.querySelector(".open-pack__button");

pack.onclick = function() {

	if (!pack.classList.contains("open-pack__button_active")) {

		let info = document.querySelector(".open-pack__info");
		let btn_next = document.querySelector(".open-pack__next");
		let result = document.querySelector(".open-pack__result");
		let card = document.querySelector(".card__img");

		info.classList.add("open-pack__info_active");
		setTimeout(() => info.classList.add("display-none"), 1000);

		card.classList.add("card__img_active");
		setTimeout(() => card.classList.remove("display-none"), 3000);

		pack.classList.add("open-pack__button_active");

		btn_next.classList.add("open-pack__next_active");
		setTimeout(() => result.classList.add("open-pack__result_active"), 1000);
	}
};