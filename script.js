document.getElementById('rss-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const url = document.getElementById('rss-url').value;
    
    fetch(`https://api.rss2json.com/v1/api.json?rss_url=${encodeURIComponent(url)}`)
        .then(response => response.json())
        .then(data => {
            const feed = data.items;
            let output = '';

            feed.forEach(item => {
                output += `
                    <div class="feed-item">
                        <h2>${item.title}</h2>
                        <p>${item.description}</p>
                        <a href="${item.link}" target="_blank">Read more</a>
                    </div>
                `;
            });

            document.getElementById('rss-feed').innerHTML = output;
        })
        .catch(error => console.error('Error fetching RSS feed:', error));
});
