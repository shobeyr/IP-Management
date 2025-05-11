async function searchData() {
    const query = document.getElementById("searchBox").value;
    const response = await fetch(`/api/groups/?q=${query}`);
    const data = await response.json();
    const results = document.getElementById("results");
    results.innerHTML = data.map(group => `<div>${group.name}</div>`).join('');
}
