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

// Clean everything else out and try this exact block
window.onload = function() {
    const btn = document.getElementById('profile-btn');
    const menu = document.getElementById('profile-dropdown');

    if (btn && menu) {
        btn.onclick = function(e) {
            e.stopPropagation(); // Stops the click from hitting the window
            console.log("Button clicked!"); // Look for this in the Console!
            menu.classList.toggle('active');
        };

        window.onclick = function() {
            console.log("Window clicked - closing menu");
            menu.classList.remove('active');
        };
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
