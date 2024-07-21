function generateCookieId() {
    return Math.random().toString(10).substring(1, 8);
}

function setCookie(name, value, days) {
    document.cookie = `${name}=${value}; expires=${new Date(Date.now() + days * 24 * 60 * 60 * 1000).toUTCString()}; path=/`;
}


function getUserId() {

    if (document.cookie.includes("userId")) {

        return document.cookie.split('; ').find(cookie => cookie.startsWith("userId=")).split('=')[1];
    } else {

        return null;
    }
}


function initializeUserId() {

    if (!document.cookie.includes("userId")) {

        let userId = generateCookieId();

        setCookie("userId", userId, 30);
    }
}


window.onload = function () {
    initializeUserId();
    const userId = getUserId();

};
