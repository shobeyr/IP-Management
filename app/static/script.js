function searchIP() {
    let input = document.getElementById('search-box').value.toLowerCase();
    let ips = document.getElementsByClassName('ip-item');

    for (let ip of ips) {
        if (ip.innerText.toLowerCase().includes(input)) {
            ip.style.display = '';
        } else {
            ip.style.display = 'none';
        }
    }
}
