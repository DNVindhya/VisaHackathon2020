/**********************************
 * 
 * Deliberately chose not to create
 * a recursive function for creating
 * dom nodes with children since the
 * javascript rendering of dom nodes
 * didn't need to be generalized enough
 * to warrant putting in the time to create
 * a generalized node rendering function.
 * 
 * That would effectively have meant 
 * creating my own javascript framework
 * for this small code test.
 * 
 * For the same reason I didn't separate
 * out code into a MVC pattern.  Wanted
 * to keep the javascript as pure vanilla
 * ES6 and a semi-functional 
 * programming pattern. 
 * 
 * Didn't use an
 * OOP approach because the size and 
 * complexity of the app didn't seem
 * to warrant using ES6 classes or 
 * ES5 objects, and because most of the
 * app focused on dom manipulation
 * of just a few core items
 * that in a larger app I might
 * have modeled as classes.
 * i.e. cards and transactions 
 * 
 * Minus initialization all of 
 * the functions are in
 * alphabetical order 
 * 
 **********************************/

'use strict'

// holds what card is active in order to display correct transactions
let state = {
  activeCard: 0
}

document.addEventListener("DOMContentLoaded", function(event) {
  /************************************************************
   * 
   * Create cards then create transactions for 
   * the active card.  Hide the loading text as well.
   * 
   ***********************************************************/

  let loading = document.querySelector('.app__loading');

  loading.style.display = 'none';

  createItems(data.cards, '.app__cards-list', createCard);

  createTransactions(state.activeCard);
});

function addChildren(parent, children) {
  /************************************************************
   * 
   * Takes a list of children and appends it to a parent node
   * 
   ***********************************************************/

  children.forEach((child) => {
    parent.appendChild(child)
  });

  return parent;
}


function createAmount(amount, colorClass) {
  /************************************************************
   * 
   * Separates the price into two elements and then applies 
   * correct classes for formatting so that the cents
   * are appropriately superscript
   * 
   ***********************************************************/

  let amountArray = amount.split('.');
  let amountElement = createElement('P', '', 'transaction__amount');
  amountElement.classList.add(colorClass);

  let amountBig = createElement('SPAN', `$${amountArray[0]}`, 'amount__big');
  let amountSmall = createElement('SPAN', `.${amountArray[1]}`, 'amount__small');

  amountElement = addChildren(amountElement, [amountBig, amountSmall]);

  return amountElement;
}


function createCard(card) {
  /************************************************************
   * 
   * Creates a card node and appends it to the card list
   * 
   ***********************************************************/

  let cardClassName = 'app__card';

  // sets appropriate class for active card

  if (state.activeCard === card.id) {
    cardClassName = 'app__card app__card--active';
  }

  let main = createElement('LI', '', cardClassName);
  main.id = card.id;

  // sets card id for click event to manage changing cards 

  main.addEventListener('click', handleClick.bind(null, card.id));

  let children = [];
  children.push(createImg(card.type));

  const cardNumber = createCardNumber(card.type, card.number);
  children.push(createElement('P', cardNumber, 'card__number'));

  const validText = `Valid Thru: ${card.validThru}`;
  children.push(createElement('P', validText, 'card__valid'));

  main = addChildren(main, children);
  let list = document.querySelector('.app__cards-list');

  list.appendChild(main);
}


function createCardNumber(type, number) {
  /************************************************************
   * 
   * Get correctly formatted card number based on card type.
   * Highly unlikely a full card number would be passed through
   * for the front end to process, but I was bored and wanted
   * to do some formatting.
   * 
   ***********************************************************/

  let cardNumber = '';
  let numberToString = String(number);

  if (type === 'amex') {
    cardNumber = `**** ****** ${numberToString.substr(numberToString.length - 5)}`
  } else {
    cardNumber = `**** **** **** ${numberToString.substr(numberToString.length - 4)}`
  }

  return cardNumber;
}


function createElement(element, txt, className) {
  /************************************************************
   * 
   * Create an element with a text node
   * 
   ***********************************************************/

  let ele = document.createElement(element);
  if (txt !== '') {
    let textNode = document.createTextNode(txt);
    ele.appendChild(textNode);
  }

  ele.className = className;

  return ele;
}


function createImg(type) {
  /************************************************************
   * 
   * Set the correct src and alt based on which card it is.
   * This does leave open the possibility of incorrect data
   * coming through and thus rendering a wrong image, but for
   * the purposes of this code test I assumed pristine data
   * for the sake of expediency. Otherwise I would add a 
   * default switch case that loads a default image if one
   * could not be found from the type input.
   * 
   ***********************************************************/

  let imgUrl = '/images/visa.png';
  let alt = '';

  switch (type) {
    case 'visa':
      imgUrl = 'visa.png';
      alt = 'visa card';
      break;
    case 'mastercard':
      imgUrl = 'mastercard.png';
      alt = 'mastercard';
      break;
    case 'amex':
      imgUrl = 'amex.png';
      alt = 'american express card';
      break;
  }

  const img = document.createElement('IMG');
  img.src = '/static/images/visa.png';
  img.alt = alt;
  img.className = 'card__img'

  return img;
}


function createInfoText({
  type,
  number,
  date
}) {
  /************************************************************
   * 
   * Create a properly formatted string with the correct info.
   * The whole transaction object is being passed in but I am 
   * using destructuring to only pull the values I need.  It 
   * greately simplifies the call to the function and passes
   * the parsing of what is useful to the function using it.
   * 
   ***********************************************************/

  const monthNames = ['January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
  ];

  let formattedDate = `${date.getDate()} ${monthNames[date.getMonth()]} ${date.getFullYear()}`;

  if (type.length === 0) {
    return `${type} ${number} - ${formattedDate}`;
  } else {
    return `${number} - ${formattedDate}`;
  }
}


function createItems(items, parentClass, callback) {
  /************************************************************
   * 
   * Clear current nodes and cycle through each new item and
   * call function to add node parent
   * 
   ***********************************************************/

  let parentNode = document.querySelector(parentClass);
  removeChildren(parentNode);

  items.forEach((item) => {
    callback(item);
  });
}


function createTransaction(transaction) {
  /************************************************************
   * 
   * Creates three columns and assigns them values based on the
   * transaction object.  It then appends to the proper list
   * node
   * 
   ***********************************************************/

  let main = createElement('LI', '', 'app__transaction');
  let children = [];

  // creates the 3 columns within the main element
  let leftCol = createElement('SECTION', '', 'transaction__left');
  let middleCol = createElement('SECTION', '', 'transaction__middle');
  let rightCol = createElement('SECTION', '', 'transaction__right');

  let symbol = '-';
  let colorClass = 'transaction__debit';

  // deal with the styling differences of a credit vs a debit
  if (transaction.action === 'credit') {
    symbol = '+';
    colorClass = 'transaction__credit';
  }

  let symbolElement = createElement('SPAN', symbol, 'transaction__symbol');
  leftCol.appendChild(symbolElement);

  let description = createElement('H3', transaction.description, 'transaction__description');
  let infoText = createInfoText(transaction);
  let infoTextElement = createElement('P', infoText, 'transaction__info-text');
  middleCol = addChildren(middleCol, [description, infoTextElement]);

  let amount = createAmount(transaction.amount, colorClass);
  rightCol.appendChild(amount);

  main = addChildren(main, [leftCol, middleCol, rightCol]);
  let node = document.querySelector('.app__transactions-list');
  node.appendChild(main);

}


function createTotal(transactions, creditAmount) {
  /************************************************************
   * 
   * Add the total of the transactions
   * 
   ***********************************************************/

  // maps over each transaction, pulls the amount (determines if credit or debit) and then adds up all the amounts to reach a total. 
  let transactionTotal = transactions.map((transaction) => transaction.action === 'credit' ? parseFloat(transaction.amount) : -parseFloat(transaction.amount)).reduce((total, num) => total + num);
  let earned_karma_points = transactions.map((transaction) => transaction.action === 'debit' ? parseFloat(transaction.karmapoints) : -parseFloat(transaction.karmapoints)).reduce((total, num) => total + num);
  // adds transactions net sum to arbitrary credit limit assigned in data.js
  let total = transactionTotal + creditAmount;
  let karma_total = earned_karma_points;
  let node = document.querySelector('.header__balance');
  let totalText = document.createTextNode(`$${total},${karma_total}`);
  removeChildren(node);
  node.appendChild(totalText);
}


function createTransactions(id) {
  /************************************************************
   * 
   * Filter out active card and then create transactions
   * 
   ***********************************************************/

  let card = data.cards.filter((card) => card.id === id);
  createItems(card[0].transactions, '.app__transactions-list', createTransaction);
  createTotal(card[0].transactions, card[0].creditAmount);
  // createKarmaTotal(card[0].transactions);
}


function handleClick(id) {
  /************************************************************
   * 
   * Change state and rerender cards and transactions
   * 
   ***********************************************************/

  state.activeCard = id;
  createItems(data.cards, '.app__cards-list', createCard);

  createTransactions(state.activeCard);
}


function removeChildren(parentNode) {
  /************************************************************
   * 
   * Remove all children of a parent node
   * 
   ***********************************************************/

  while (parentNode.firstChild) {
    parentNode.removeChild(parentNode.firstChild);
  }
}