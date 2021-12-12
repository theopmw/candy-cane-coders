const showAdmin = ['/', '/accounts/login/', '/accounts/logout/', '/accounts/signup/'].some(path => path == window.location.pathname);


function navBarMenu() {
    let x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

if (!showAdmin && document.getElementById('admin-add-day')) {
    document.getElementById('admin-add-day').addEventListener('click', () => addDay());
    document.getElementById('admin-secret-santa').addEventListener('click', () => setDay11());
    document.getElementById('admin-reset').addEventListener('click', () => resetDraw());
}

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
            if (data.status == 401) {
                UIkit.notification({
                    message: `You are not Authorised`,
                    status: 'primary',
                    pos: 'top-right',
                    timeout: 5000
                });
            }
            else if (data.status == 200) {
                UIkit.notification({
                    message: `Day +1 actioned`,
                    status: 'primary',
                    pos: 'top-right',
                    timeout: 5000
                });
                setTimeout(() => window.location.reload(), 2500);
            }
            else if (data.status == 406) {
                UIkit.notification({
                    message: data.message,
                    status: 'primary',
                    pos: 'top-right',
                    timeout: 5000
                });
            };
        })
        .catch(err => console.log(err));
};

function setDay11() {
    fetch(`/draw/set_day_11/`, {
            method: 'POST',
            headers: new Headers({
                'X-CSRFToken': csrftoken,
            }),
            credentials: 'same-origin',
        })
        .then(res => res.json())
        .then(data => {
            if (data.status === 200) {
                UIkit.notification({
                    message: `Day set to 11 and Secret Santa drawn`,
                    status: 'primary',
                    pos: 'top-right',
                    timeout: 2500
                });
                setTimeout(() => window.location.reload(), 2500);
            }
            else if (data.status === 401) {
                UIkit.notification({
                    message: `You are not Authorised`,
                    status: 'primary',
                    pos: 'top-right',
                    timeout: 5000
                });
            };
        })
        .catch(err => console.log(err));
};

function resetDraw() {
    fetch(`/draw/reset_draw/`, {
            method: 'POST',
            headers: new Headers({
                'X-CSRFToken': csrftoken,
            }),
            credentials: 'same-origin',
        })
        .then(res => res.json())
        .then(data => {
            if (data.status === 200) {
                UIkit.notification({
                    message: `Draw has been reset`,
                    status: 'primary',
                    pos: 'top-right',
                    timeout: 2500
                });
                setTimeout(() => window.location.reload(), 2500);
            }
            else if (data.status === 401) {
                UIkit.notification({
                    message: `You are not Authorised`,
                    status: 'primary',
                    pos: 'top-right',
                    timeout: 5000
                });
            };
        })
        .catch(err => console.log(err));
};