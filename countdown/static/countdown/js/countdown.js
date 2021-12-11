// gifts event listener
const gifts = document.querySelectorAll('.gift');
gifts.forEach(gift => gift.addEventListener('click', event => {
    // get the id of the gift
    const gift_id = event.currentTarget.dataset.gift_id;
    // call the post function
    userChoseGift(gift_id)
}));

// post gift to backend
function userChoseGift(gift_id) {
    // post to backend
    fetch(`/wishlists/add_to_wishlist/${gift_id}/`, {
        method: 'POST',
        headers: new Headers({
            'X-CSRFToken': csrftoken,
        }),
        credentials: 'same-origin',
    })
    .then(res => res.json())   
    .then(data => {
        // the returned data from the backend
        console.log(data);
        // now you should disable the gift from being clicked again
        // now you should show a notification that the gift has been added to wishlist with the gift name etc...
        UIkit.notification({
            message: `Gift ${data.gift_id} has been added to your wishlist!`,
            status: 'primary',
            pos: 'top-right',
            timeout: 5000
        });
    })
    .catch(err => console.log(err));
};
