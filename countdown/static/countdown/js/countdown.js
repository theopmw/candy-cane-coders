// gifts event listener
let multipleClick = false;
let list = false;
let pickedList = [];
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
            let pGiftId = "gift" + data.gift_id;
            document.getElementById(pGiftId).innerText = "Added to Wishlist";
            list = false;
            for (let j = 0; j <= pickedList.length; j++) {
                if (data.gift_id == pickedList[j]) {
                    list = true;
                }
            }
            if (!multipleClick || !list) {
                multipleClick = true;
                pickedList.push(data.gift_id);
                // now you should show a notification that the gift has been added to wishlist with the gift name etc...
                UIkit.notification({
                    message: `Gift ${data.gift_id} has been added to your wishlist!`,
                    status: 'primary',
                    pos: 'top-right',
                    timeout: 5000
                });
            } else { // now you should disable the gift from being clicked again
                document.querySelector(`[data-gift_id="${data.gift_id}"]`).style.clickEvents = "none";
            }

        })
        .catch(err => console.log(err));
};