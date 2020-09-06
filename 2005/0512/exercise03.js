let day = 2
if (day === 1) {
    console.log('월요일')
} else if (day === 2) {
    console.log('화요일')
} else if (day === 3) {
    console.log('수요일')
} else if (day === 4) {
    console.log('목요일')
} else if (day === 5) {
    console.log('금요일')
} else if (day === 6) {
    console.log('토요일')
} else {
    console.log('일요일')
}

// switch 활용할 때는
// break 꼭 넣어야 한다

switch(day){
    case 1:{
        console.log('월요일')
        break
    }
    case 2:{
        console.log('화요일')
        break
    }
    case 3:{
        console.log('수요일')
        break
    }
    case 4:{
        console.log('목요일')
        break
    }
    case 5:{
        console.log('금요일')
        break
    }
    case 6:{
        console.log('토요일')
        break
    }
    default:{
        console.log('일요일')
        break
    }
}

let i = 0
while (i<6){
    console.log(i++)
    //i++
}

for (let i=0; i<6; i++){
    console.log(i)
}

const numbers = [0, 1, 2, 3, 4]
for (const number of numbers){
    console.log(number)
}

const fruits = {
    'apple':2,
    'banana':10,
    'tomato':10,
    'watermelon':2,
}

for (const key in fruits) {
    console.log(key, fruits[key])
}
// Object.entries(fruits)
// fruits.valueOf()

for (let i = 0; i<10; i++){
    if (i===3){
        continue
    }
    console.log(i)
}