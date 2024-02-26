const people = [
  {"id": 1, "name": "John", "age": 25, "city": "New York"},
  {"id": 2, "name": "Alice", "age": 30, "city": "San Francisco"},
  {"id": 3, "name": "Bob", "age": 28, "city": "Los Angeles"},
  {"id": 4, "name": "Emily", "age": 22, "city": "Chicago"},
  {"id": 5, "name": "Michael", "age": 35, "city": "Seattle"},
  {"id": 6, "name": "Sophia", "age": 27, "city": "Boston"},
  {"id": 7, "name": "David", "age": 31, "city": "Miami"},
  {"id": 8, "name": "Olivia", "age": 26, "city": "Austin"},
  {"id": 9, "name": "Daniel", "age": 29, "city": "Denver"},
  {"id": 10, "name": "Ella", "age": 24, "city": "Portland"}
]

function compareByName(a, b) {
  return a.name.localeCompare(b.name);
}

people.sort(compareByName);

console.log(people)

console.log(people.filter(x => x.age > 30));

const peopledisplay = document.getElementById('display')

people.forEach((person) => {
  console.log(`${person.name} (${person.age})`)
  const li = document.createElement('li');
  const text = document.createTextNode(`${person.name} (${person.age})`)

  li.appendChild(text);
  peopledisplay.appendChild(li);
})

const cities = people.map(x => x.city);

const citiesdisplay = document.getElementById('cities');

citiesdisplay.innerText = cities

console.log(cities);