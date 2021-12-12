//nav bar
function navBarMenu() {
    let x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

// Admin

const dayPlusOne = document.getElementByID('admin-add-day');
dayPlusOne.addEventListener('click', event => {
    addDay();
});

const initiateSecretSanta = document.getElementByID('admin-secret-santa');
initiateSecretSanta.addEventListener('click', event => {
    secretSantaDraw();
});

const resetTimer = document.getElementByID('admin-reset');
resetTimer.addEventListener('click', event => {
    resetDay();
});

function addDay() {
    fetch(`/draw/increase_day/`, {
            method: 'POST',
            headers: new Headers({
                'X-CSRFToken': csrftoken,
            }),
            credentials: 'same-origin',
        })
        .then(res => res.json())
        .then(data => {
            UIkit.notification({
                message: `Day +1 actioned`,
                status: 'primary',
                pos: 'top-right',
                timeout: 5000
            });

        })
        .catch(err => console.log(err));
};

function secretSantaDraw() {
    fetch(`/draw/increase_day/`, {
            method: 'POST',
            headers: new Headers({
                'X-CSRFToken': csrftoken,
            }),
            credentials: 'same-origin',
        })
        .then(res => res.json())
        .then(data => {
            UIkit.notification({
                message: `Day set to 11 and Secret Santa drawn`,
                status: 'primary',
                pos: 'top-right',
                timeout: 5000
            });

        })
        .catch(err => console.log(err));
};

function resetDay() {
    fetch(`/draw/increase_day/`, {
            method: 'POST',
            headers: new Headers({
                'X-CSRFToken': csrftoken,
            }),
            credentials: 'same-origin',
        })
        .then(res => res.json())
        .then(data => {
            UIkit.notification({
                message: `Day set to 1, Secret Santa draw reset`,
                status: 'primary',
                pos: 'top-right',
                timeout: 5000
            });

        })
        .catch(err => console.log(err));
};