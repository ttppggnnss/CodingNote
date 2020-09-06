const numbers = [ 1, 2, 3, 4 ]

// const numbers[0]
// 이렇게 안된다
numbers[0]
numbers[-1]
// 음수는 정의도지 않는다
numbers.length
numbers.reverse()
numbers
numbers.reverse()
numbers
numbers.push('a')
numbers.pop()
numbers.unshift('a')
numbers
numbers.shift()
numbers.includes(1)
numbers.includes(0)
numbers.push('a','a')
numbers.indexOf('a')
numbers.indexOf('b')
numbers.join()
numbers.join('')
numbers.join('-')

const me = {
  name: '변승환',
  'phone number': '01012345678',
  equipment:{
    phone:'ga17',
    macbook:'2019pro',
  },
}

me.name

me['name']
me['phone number']
// 이름이 두 단어 이상인 경우
// 대괄호로 접근해야한다.

me.equipment
me.equipment.phone

const fruits = {a: 'apple', b: 'banana'}

Object.keys(fruits)

Object.values(fruits)

Object.entries(fruits)

let books = ['Learning Js', 'Eloquent JS']

let comics = {
  DC:['AquaMan', 'SHAZAM'],
  Marvel: ['Captain Marvel', 'Avengers'],
}
const bookshop = {
  books: books,
  comics: comics,
}

// key value 같은 경우
// 한 번만 적어도 된다
const bookShop =  {
  books,
  comics,
}

console.log(typeof bookShop)

console.log(bookShop.books[0])

const jsonData = JSON.stringify({
  coffee: 'Americano',
  iceCream: 'Cookie and cream',
})

console.log(jsonData)

console.log(typeof(jsonData))

const parsedData = JSON.parse(jsonData)
console.log(parsedData)
console.log(typeof(parsedData))

const colors = ['red', 'green', 'blue',]

colors.forEach(function(color){
  console.log(color)
})


for (const number of numbers) {
  console.log(number)
}
// const 로 하든 let 으로 하든 상관 없다

colors.forEach(color => console.log(color))




const images = [
  {height: 10, width:30}, 
  {height:20, width:90},
]

const areas = []

images.forEach(function(image){
  areas.push(image.height * image.width)
})

console.log(areas)




const numbers = [1, 2, 3]

const doublenumbers = numbers.map(function(number){
  return number *2
})
console.log(doublenumbers)

const newNumbers = [4, 9, 16]

const roots = newNumbers.map(Math.sqrt)

console.log(roots)

const products = [
  {name: 'cocumber', type: 'vegetable'},
  {name: 'banana', type: 'fruit'},
  {name: 'carrot', type: 'vegetable'},
  {name: 'apple', type: 'fruit'},
]

const fruits = products.filter(function(product){
  return product.type === 'fruit'
})

console.log(fruits)

const numbers2 = [15, 25, 35, 45, 55, 65, 75, 85, 95]

const filterNumbers2 = numbers2.filter(function(number){
  return number > 50
})


const people = [
  { id: 1, admin: false},
  { id: 2, admin: false},
  { id: 3, admin: true},
]

const admin = people.find(function(person){
  return person.admin === true
})

console.log(admin)

const people1 = [
  { id: 1, admin: false},
  { id: 2, admin: false},
  { id: 3, admin: false},
]

const admin1 = people1.find(function(person){
  return person.admin === true
})

console.log(admin1)


const arr = [1,2,3,4,5]

const result = arr.some(elem => elem % 2 === 0)

console.log(result)

const result2 = arr.some(elem => elem % 6 === 0)

console.log(result2)

const result3 = arr.every(elem => elem % 2 === 0)

console.log(result3)

