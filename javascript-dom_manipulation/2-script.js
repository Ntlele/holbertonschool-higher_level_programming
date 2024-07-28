const myHeader = document.body.querySelector("header");

const theClick = document.body.querySelector("red_header");
theClick.addEventListener("click", () => {
    theClick.classList.add("red");
});