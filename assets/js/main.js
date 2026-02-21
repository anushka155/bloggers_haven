// Dark/Light Mode Toggle

document .addEventListener('DOMContentLoaded', () => {let darkmode = localStorage.getItem('darkmode');
const themeSwitch = document.getElementById('theme-switch');

const enableDarkmode = () => {
    document.body.classList.add('darkmode');
    localStorage.setItem('darkmode', 'active');
}

const disableDarkmode = () => {
    document.body.classList.remove('darkmode');
    localStorage.setItem('darkmode', 'inactive');
}

if (darkmode === "active") {
    enableDarkmode();
}

themeSwitch.addEventListener('click', function() {
    darkmode = localStorage.getItem('darkmode');
    darkmode !== "active" ? enableDarkmode() : disableDarkmode();
});
});


// Profile Dropdown Toggle

window.onload = function() {
    const btn = document.getElementById('profile-btn');
    const menu = document.getElementById('profile-dropdown');

    if (btn && menu) {
        btn.onclick = function(e) {
            e.stopPropagation(); 
            console.log("Button clicked!"); 
            menu.classList.toggle('active');
        };

        window.addEventListener("click", function() {
        console.log("Window clicked - closing menu");
        menu.classList.remove('active');
        });

    } else {
        console.log("Error: Could not find button or menu IDs");
    }
};

// Menu Toggle

const menuToggle = document.getElementById("menu-toggle");
const sidebar = document.getElementById("sidebar");

menuToggle.addEventListener("click", () => {
  sidebar.classList.toggle("active");
  document.body.classList.toggle("sidebar-open");
});


// Like Button AJAX

document.addEventListener('DOMContentLoaded', function() {
    const button = document.getElementById('like-button');

    if (!button) return;

    button.addEventListener('click', function() {

        fetch(button.dataset.url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            location.reload();
        });

    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}