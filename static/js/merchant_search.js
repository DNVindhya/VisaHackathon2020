// https://hp-api.herokuapp.com/api/characters
// "{% url '/customer/earn_offers' merchant.merchant_id %}"
// <h5> ${merchant.merchant_id} </h1>
const merchantList = document.getElementById('merchantList');
const searchBar = document.getElementById('searchBar');
let listmerchants = [];

searchBar.addEventListener('keyup', (e) => {
    const searchString = e.target.value.toLowerCase();

    const filteredCharacters = listmerchants.filter((merchant) => {
        return (
            merchant.merchant_name.toLowerCase().includes(searchString) ||
            merchant.address.toLowerCase().includes(searchString)
        );
    });
    displayCharacters(filteredCharacters);
});

const loadCharacters = async () => {
    try {
        const res = await fetch('/customer/earn_karma_points');
        console.log("Success")
        listmerchants = await res.json();
        displayCharacters(listmerchants);

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
                    <h6>${merchant.merchant_name}</h6>
                    <p>Address: ${merchant.address}</p>
                    <p>Offers: ${merchant.offers}</p>
                    </button>
                </li>
            </a>
        `;

        })
        .join('');
    merchantList.innerHTML = htmlString;
};

loadCharacters();
