let pairs = [];
let page = 0;
let max_pages = 0;
const results_container = document.querySelector(".results");
const input = document.querySelector(".input");
const search_button = document.querySelector(".search-button");
const next_page = document.querySelector("#next");
const prev_page = document.querySelector("#prev");

const pairCard = (pair) => `
    <div class="pair">
        <p>${pair[0]}</p>
        <p>${pair[1]}</p>
    </div>`;

const displayCharacters = () => {
    results_container.innerHTML = "";
    let actual_pairs;
    if (pairs.length > 10) {
        const lower = page*10;
        const upper = lower + 10;
        actual_pairs = pairs.slice(lower, upper);
        max_pages = Math.floor(pairs.length/10);
        if (page == 0) next_page.disabled = false;
    } else {
        actual_pairs = pairs;
        next_page.disabled = true;
        prev_page.disabled = true;
    }
    for (let pair of actual_pairs) {
        results_container.innerHTML += pairCard(pair);
    }
}

const change_page = (e) => {
    const button = e.currentTarget;
    if(!button.disabled) {
        (button.id == "next")
            ? page ++
            : page --;
        if (page == 0) {
            prev_page.disabled = true;
            next_page.disabled = false;
        } else if (page == max_pages) {
            prev_page.disabled = false;
            next_page.disabled = true;
        } else {
            prev_page.disabled = false;
            next_page.disabled = false;
        }
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
                prev_page.disabled = true;
                next_page.disabled = true;
                displayCharacters();
            } else {
                results_container.innerHTML = `<p class="error-message">${data.message}</p>`;
            }
        })
        .catch(error => console.error(error));
}

search_button.addEventListener('click', getPairs);
prev_page.addEventListener("click", change_page);
next_page.addEventListener("click", change_page);