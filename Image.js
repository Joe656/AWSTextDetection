function sendHttpRequest() {
    
    const imageFile = document.getElementById('imageFile').files[0];
    const cookieId = getCookie('userId');
    
   
    const formData = new FormData();
    formData.append('imageFile', imageFile);
   
    const headers = new Headers();
    headers.append('Content-Type', 'multipart/form-data');
    headers.append('Cookie', `userId=${cookieId}`); 
    //sends to text_image_detection
    fetch(upload, {
        method: 'POST',
        headers: headers,
        body: formData
    })
    window.location.href = 'index.html';
}
function getCookie(name) {
    const cookies = document.cookie.split('; ');
    for (const cookie of cookies) {
        const [cookieName, cookieValue] = cookie.split('=');
        if (cookieName === name) {
            return decodeURIComponent(cookieValue);
        }
    }
    return null;
}

