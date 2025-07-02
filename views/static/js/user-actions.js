document.getElementById('search-bar').addEventListener('input', function () {
    const query = this.value;

    fetch(`/backoffice/search?query=${encodeURIComponent(query)}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch user data.');
            }
            return response.text();
        })
        .then(html => {
            document.getElementById('users-list').innerHTML = html;
        })
        .catch(error => {
            document.getElementById('users-list').innerHTML = '<p>Error loading data. Please try again later.</p>';
        });
});
