let multipleClick = false;
let list = false;
let pickedList = [];

const gifts = document.querySelectorAll('.gift');
gifts.forEach(gift => gift.addEventListener('click', event => {
    const gift_id = event.currentTarget.dataset.gift_id;
    userChoseGift(gift_id);
}));

function userChoseGift(gift_id) {
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
        document.getElementById(pGiftId).innerHTML = '<span class="uk-text-danger">Already in Wishlist</span>';
        list = false;
        for (let j = 0; j <= pickedList.length; j++) {
            if (data.gift_id == pickedList[j]) list = true;
        }
        if (!multipleClick || !list) {
            multipleClick = true;
            pickedList.push(data.gift_id);

            UIkit.notification({
                message: `Day ${data.gift_id}'s gift has been added to your wishlist!`,
                status: 'primary',
                pos: 'top-right',
                timeout: 5000
            });
        } else { 
            document.querySelector(`[data-gift_id="${data.gift_id}"]`).style.clickEvents = "none";
        }

    })
    .catch(err => console.log(err));
};