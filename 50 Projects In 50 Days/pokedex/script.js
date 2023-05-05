const poke_container = document.getElementById('poke-container')

const pokemon_count = 150

//add missing types? (e.g. steel and dark) 
// color of two types? Combination, gradient or half-half?
const colors = {
    fire: '#FDDFDF',
    grass: '#DEFDE0',
	electric: '#FCF7DE',
	water: '#DEF3FD',
	ground: '#f4e7da',
	rock: '#d5d5d4',
	fairy: '#fceaff',
	poison: '#98d7a5',
	bug: '#f8d5a3',
	dragon: '#97b3e6',
	psychic: '#eaeda1',
	flying: '#F5F5F5',
	fighting: '#E6E0D4',
	normal: '#F5F5F5'
}

const main_types = Object.keys(colors)
//console.log(main_types)


//Get the pokemons from the Hoenn region?

const fetchPokemons = async () => {
    for(let i = 1; i <= pokemon_count; i++) {
        await getPokemon(i)
    }
}

// Can be optimized by getting multiple pokemons for each request
// TODO: Try to do this
const getPokemon = async (id) => {
    const url = `https://pokeapi.co/api/v2/pokemon/${id}`
    const res = await fetch(url)
    const data = await res.json()
    //console.log(data)

    createPokemonCard(data)
}

const createPokemonCard = (pokemon) => {
    const pokemonEl = document.createElement('div')
    pokemonEl.classList.add('pokemon')

    // Get name. Make first letter uppercase
    const name = pokemon.name[0].toUpperCase() + pokemon.name.slice(1);

    // Get ID. Add leading zeros
    const id = pokemon.id.toString().padStart(3, '0')

    // Get both types for pokemons with 2 types?
    //console.log(pokemon.types)
    const poke_types = pokemon.types.map(type => type.type.name)
    //console.log(poke_types)
    const type = main_types.find(type => poke_types.indexOf(type) > -1)
    //console.log(type)
    const color = colors[type]

    pokemonEl.style.backgroundColor = color;


    const pokemonInnerHTML = `
        <div class="img-container">
            <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${pokemon.id}.png" alt="">
        </div>
        <div class="info">
            <span class="number">#${id}</span>
            <h3 class="name">${name}</h3>
            <small class="type">Type: <span>${type}</span></small>
        </div>
    `

    pokemonEl.innerHTML = pokemonInnerHTML

    poke_container.appendChild(pokemonEl)
}

fetchPokemons()