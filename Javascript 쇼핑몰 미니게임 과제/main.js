function loadItems() {
    return fetch('./data.json')
        .then(Response => Response.json())
        .then(json => json.items);
}

function displayItems(items) {
    const container = document.querySelector('.items');
    container.innerHTML = items.map(item => createHTMLString(item)).join('')
}

function createHTMLString(item) {
    return `
    <li class="item">
            <img src="${item.image}" alt="${item.type}" class="item_thumbnail">
            <span class="item_description">${item.gender}, ${item.size}</span>
        </li>    
    `;
}

function onButtonClick(event, items) {
    const dataset = event.target.dataset;
    const key = dataset.key;
    const value = dataset.value;

    if(key == null || value == null) {
        return;
    
    }

    const filtered = items.filter(item => item[key] === value);
    displayItems(filtered);

    //updateItems(items, key, value);
}

// function updateItems(items, key, value) {
//     items.forEach(item => {
//         if(item.dataset[key] === value) {
//             item.classList.remove('invisible');
//         } else {
//             item.classList.add('invisible');
//         }
        
//     })
// }
function setEventListeners(items) {
    const logo = document.querySelector('.logo');
    const buttons = document.querySelector('.buttons');
    logo.addEventListener('click', () => displayItems(items));
    buttons.addEventListener('click', event => onButtonClick(event, items));
}
loadItems()
    .then(items => {
        console.log(items);
        displayItems(items);
        setEventListeners(items);
    })
    .catch(console.log);