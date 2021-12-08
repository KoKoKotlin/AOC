const fs = require("fs")

function loss_function1(x, param) {
    let res = 0
    for (let i = 0; i < x.length; i++) {
        res += Math.abs(x[i] - param)
    }

    return res
}

function gradient1(x, param) {
    let res = 0
    for (let i = 0; i < x.length; i++) {
        res += (x[i] - param > 0) ? -1 : 1
    }

    return res
}

function gradient_descent1(x) {
    let param = 0
    let iterations = 0
    let learning_rate = 0.01
    
    while(iterations++ < 1000) {
        param = param - learning_rate * gradient1(x, param)
    }
    
    return Math.round(param)
}

function solve1(data) {
    data = data.split(",").map((s => parseInt(s)))
    let best_point = gradient_descent1(data)

    console.log(`Solution 1: ${loss_function1(data, best_point)}`)
}


function loss_function2(x, param) {
    let res = 0
    for (let i = 0; i < x.length; i++) {
        n = Math.abs(x[i] - param)
        res += 0.5 * n * (n + 1)
    }

    return res
}

function gradient2(x, param) {
    let res = 0
    for (let i = 0; i < x.length; i++) {
        const val = x[i] - param
        res += 0.5 * (-Math.sign(val) * (Math.abs(val) + 1) - Math.sign(val) * Math.abs(val))
    }

    return res
}

function gradient_descent2(x) {
    let param = 100
    let iterations = 0
    let learning_rate = 0.001
    
    while(iterations++ < 1000) {
        param = param - learning_rate * gradient2(x, param)
    }
    
    return Math.round(param)
}

function solve2(data) {
    data = data.split(",").map((s => parseInt(s)))
    let best_point = gradient_descent2(data)

    console.log(`Solution 2: ${loss_function2(data, best_point)}`)
}

const data = fs.readFileSync("data.txt").toString()
solve1(data)
solve2(data)
