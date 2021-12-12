
const deletes = document.querySelectorAll('.gift');
deletes.forEach(gift => gift.addEventListener('click', event => {
    const gift_id = event.currentTarget.dataset.gift_id;
    const user_id = event.currentTarget.dataset.user_id;
    const user_name = event.currentTarget.dataset.user_name;
    sendWishlistItem(gift_id, user_id, user_name);
}));

const sendWishlistItem = (gift_id, user_id, user_name) => {
    fetch(`/gifts/send/${gift_id}/${user_id}/`, {
        method: 'POST',
        headers: new Headers({
            'X-CSRFToken': csrftoken,
        }),
        credentials: 'same-origin',
    })
    .then(res => res.json())
    .then(data => {
        UIkit.notification({
            message: `You just sent ${user_name} a gift!`,
            status: 'primary',
            pos: 'top-right',
            timeout: 2000
        });

        setTimeout(() => {
            window.location.href = '/gifts/given/'
        }, 2500);
    })
    .catch(err => console.log(err));
};