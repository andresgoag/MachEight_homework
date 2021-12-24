let pairs = [];
let page = 0;
const results_container = document.querySelector(".results")
const input = document.querySelector(".input");
const search_button = document.querySelector(".search-button");
const next_page = document.querySelector("#next");
const prev_page = document.querySelector("#prev");

const pairCard = (pair) => `
    <div class="pair">
        <p>${pair[0]}</p>
        <p>${pair[1]}</p>
    </div>`

const displayCharacters = () => {
    results_container.innerHTML = "";
    let page_buttons_html = ""
    let actual_pairs;

    if (pairs.length > 10) {
        const lower = page*10
        const upper = lower + 10
        actual_pairs = pairs.slice(lower, upper)
        next_page.disabled = false;
    } else {
        actual_pairs = pairs;
    }
    for (let pair of actual_pairs) {
        results_container.innerHTML += pairCard(pair)
    }
    results_container.innerHTML += page_buttons_html;
}

const change_page = (e) => {
    const button = e.currentTarget;
    if(!button.disabled) {
        (button.id == "next")
            ? page ++
            : page --
        displayCharacters();
    }
}

const getPairs = () => {
    const target = input.value;
    if (!target) return alert("Please enter a desired total height");
    fetch(`/matching_pairs/${target}`)
        .then(resp => resp.json())
        .then(data => {
            if (data.status) {
                pairs = data.pairs;
                page = 0;
                displayCharacters();
            } else {
                results_container.innerHTML = `<p class="error-message">${data.message}</p>`
            }
        })
        .catch(error => console.error(error))
}

search_button.addEventListener('click', getPairs);
prev_page.addEventListener("click", change_page)
next_page.addEventListener("click", change_page);

