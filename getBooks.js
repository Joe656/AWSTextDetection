
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


const cookieId = getCookie('userId');


const apiUrl = api;
fetch(`${apiUrl}?cookieId=${cookieId}`)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
      
        const dataArray = JSON.parse(data.body);

       
        const myBooks = document.getElementById('myBooks');

   
        const table = document.createElement('table');

        
        const tableHeader = table.createTHead();
        const headerRow = tableHeader.insertRow();
        const headers = ['Books']; 
        headers.forEach(headerText => {
            const headerCell = headerRow.insertCell();
            headerCell.textContent = headerText;
        });

      
        const tableBody = document.createElement('tbody');
        dataArray.forEach(bookData => {
            const dataRow = tableBody.insertRow();
            const dataCell = dataRow.insertCell();
            dataCell.textContent = bookData;
        });

        
        myBooks.appendChild(table);
    })
    .catch(error => {
        console.error('Error fetching user data:', error);
    });
