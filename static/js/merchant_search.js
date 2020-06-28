// https://hp-api.herokuapp.com/api/characters
// "{% url '/customer/earn_offers' merchant.merchant_id %}"
const charactersList = document.getElementById('charactersList');
const searchBar = document.getElementById('searchBar');
let hpCharacters = [];

searchBar.addEventListener('keyup', (e) => {
    const searchString = e.target.value.toLowerCase();

    const filteredCharacters = hpCharacters.filter((character) => {
        return (
            character.name.toLowerCase().includes(searchString) ||
            character.house.toLowerCase().includes(searchString)
        );
    });
    displayCharacters(filteredCharacters);
});

const loadCharacters = async () => {
    try {
        const res = await fetch('/customer/earn_karma_points');
        console.log("Success")
        merchants = await res.json();
        displayCharacters(merchants);

    } catch (err) {
        console.error(err);
    }
};

const displayCharacters = (merchants) => {
    const htmlString = merchants
        .map((merchant) => {
            return `
            <a href="/customer/earn_offers/${merchant.merchant_id}/">
                <li class="character">
                    <h1> ${merchant.merchant_id} </h1>
                    <h2>${merchant.merchant_name}</h2>
                    <p>Address: ${merchant.address}</p>
                    <p>Offers: ${merchant.offers}</p>
                    </button>
                </li>
            </a>
        `;

        })
        .join('');
    charactersList.innerHTML = htmlString;
};

loadCharacters();
