
const deletes = document.querySelectorAll('.delete-item');
deletes.forEach(gift => gift.addEventListener('click', event => {
    const gift_id = event.currentTarget.dataset.gift_id;
    deleteWishlistItem(gift_id);
}));

const deleteWishlistItem = gift_id => {
    fetch(`/wishlists/remove_from_wishlist/${gift_id}/`, {
        method: 'POST',
        headers: new Headers({
            'X-CSRFToken': csrftoken,
        }),
        credentials: 'same-origin',
    })
        .then(res => res.json())
        .then(data => {
            reorderWishlist(data.gift_id);
            UIkit.notification({
                message: `Gift has been removed from your wishlist!`,
                status: 'primary',
                pos: 'top-right',
                timeout: 5000
            });
        })
        .catch(err => console.log(err));
};


const reorderWishlist = gift_id => {
    let count = 1;
    const items = document.querySelectorAll('.item');
    items.forEach(item => {
        if (item.dataset.gift_id == parseInt(gift_id)) item.remove()
        else {
            item.firstElementChild.innerText = `${count}. `;
            count++;
        };
    });
};