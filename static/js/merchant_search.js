// https://hp-api.herokuapp.com/api/characters
// "{% url '/customer/earn_offers' merchant.merchant_id %}"
// <h5> ${merchant.merchant_id} </h1>
const merchantList = document.getElementById('merchantList');
const searchBar = document.getElementById('searchBar');
let listmerchants = [];

function capitalizeFirstLetter(inputString) {
    return inputString.charAt(0).toUpperCase() + inputString.slice(1);
}
  

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
            <a href="/customer/earn_offers/${merchant.merchant_id}/" style="text-decoration: none!important;">
                <li class="character">
                    <h4>${capitalizeFirstLetter(merchant.merchant_name)}</h4>
                    <p>Address: <span style="font-weight:100; color: #3c3c3c;">${merchant.address}</span></p>
                    <p style="float: left; margin-top: -10px;"><b>Distance:</b> <span style="font-weight:100; color: #3c3c3c;">${merchant.distance.toFixed(1)} miles</span></p>
                    <p style="float: right; margin-top: -10px;"><b>Current Offers:</b> <span style="font-weight:100; color: #3c3c3c;">${merchant.offers.length}</span></p>
                    </button>
                </li>
            </a>
        `;

        })
        .join('');
    merchantList.innerHTML = htmlString;
};

loadCharacters();
