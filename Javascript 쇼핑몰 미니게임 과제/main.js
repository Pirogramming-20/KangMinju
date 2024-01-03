function loadItems() {
    return fetch('./data.json')
    .then(Response => Response.json())
    .then(json => json.items);
}

loadItems()
    .then(items => {
        console.log(items);
        //displayItems(items);
        //setEventListeners(items);
    })
    .catch(console.log);