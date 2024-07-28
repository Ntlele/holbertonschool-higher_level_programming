fetch('https://swapi-api.hbtn.io/api/films/?format=json')
.then(response => response.json())
.then(data => {
  const moviesList = document.getElementById('list_movies');
  data.results.forEach(film => {
    const listItem = document.createElement('li');
    listItem.textContent = film.title;
    moviesList.appendChild(listItem);
  });
})
.catch(error => console.error('Error:', error));
