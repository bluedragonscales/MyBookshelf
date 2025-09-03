// Grab the whole div with the login form.
const loginTab = document.getElementById('login');

// Grab the whole div with the register form.
const registerTab = document.getElementById('register');

// Grab the login and register tab buttons for dynamic styling.
const loginTabBtn = document.getElementById('loginTabBtn');
const registerTabBtn = document.getElementById('registerTabBtn');

// On click of the login tab button, change to the login tab form. On click of the register tab button, change to the register tab form.
function toggleLoginRegister(tab) {
    if(tab === loginTab) {
        loginTab.style.display = 'block';
        registerTab.style.display = 'none';

        // Highlight the tab button for the tab currently in focus.
        loginTabBtn.style.backgroundColor = 'rgba(7, 7, 236, 0.3)';
        registerTabBtn.style.backgroundColor = 'black';
    } else {
        registerTab.style.display = 'block';
        loginTab.style.display = 'none';

        // Highlight the tab button for the tab currently in focus.
        registerTabBtn.style.backgroundColor = 'rgba(7, 7, 236, 0.3)';
        loginTabBtn.style.backgroundColor = 'black';
    }
};