const loginTab = document.getElementById('login');
const registerTab = document.getElementById('register');

function toggleLoginRegister(tab) {
    if(tab === loginTab) {
        loginTab.style.display = 'block';
        registerTab.style.display = 'none';
    } else {
        registerTab.style.display = 'block';
        loginTab.style.display = 'none';
    }
};