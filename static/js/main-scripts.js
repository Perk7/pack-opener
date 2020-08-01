// Кнопка меню

let menu_btn = document.querySelector(".button-main-menu");

menu_btn.onclick = function() {

	let menu = document.querySelector(".main-menu");
	let list_menu = document.querySelector(".main-menu__list");
	let menu_button = document.querySelector(".button-main-menu__image");

	if (menu.classList.contains('main-menu_active')) {

			setTimeout(() => menu.classList.remove("main-menu_active"), 1000);
			setTimeout(() => menu.classList.add("main-menu_disabled"), 1000);

			menu_button.setAttribute("src", "static/img/menu-icon.svg");
			menu_button.classList.remove("button-main-menu__image_active");

			list_menu.classList.remove("main-menu__list_active");
			list_menu.classList.add("main-menu__list_disabled");
			setTimeout(() => list_menu.classList.add("display-none"), 1000);

			if (window.innerWidth >= 768 ) {
				menu_btn.classList.remove(".button-main-menu_active");
				}

		} else {

			menu.classList.remove("main-menu_disabled");
			menu.classList.add("main-menu_active");

			menu_button.setAttribute("src", "static/img/close-menu.svg");
			menu_button.classList.add("button-main-menu__image_active");

			list_menu.classList.remove("display-none");
			list_menu.classList.remove("main-menu__list_disabled");
			list_menu.classList.add("main-menu__list_active");

			if (window.innerWidth >= 768 ) {
				menu_btn.classList.add(".button-main-menu_active");
				}

		}
};