// Приближение карты

let cards = document.querySelectorAll(".collection__item");
let bg = document.querySelector(".item_active__shadow-block");

cards.forEach(card => card.addEventListener('click', function() {

	if (card.classList.contains("collection__item_active")) {

		bg.classList.add("display-none");

		card.classList.remove("collection__item_active");

	} else {

		bg.classList.remove("display-none");

		card.classList.add("collection__item_active");

	}
}
));

bg.onclick = function() {

		bg.classList.add("display-none");

		cards.forEach(card => card.classList.remove("collection__item_active"));
};