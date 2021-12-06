const fs = require("fs")

function solve1(data) {
    let all_vals = []
    data.replace(" ", "").replace("->", ",").split("\n").forEach(elem => {
        elem.split(",").map(s => parseInt(s)).forEach(i => all_vals.push(i))
    });

    const max = Math.max(...all_vals) + 1

    let grid = []
    for (let i = 0; i < max * max; i++) grid.push(0)

    const points = data.split("\n").map(str => str.replace(" ", "").split("->").map(arr_str => arr_str.split(",").map(s => parseInt(s))))
    
    points.forEach((elem => {
        let xStart = Math.min(elem[0][0], elem[1][0])
        let yStart = Math.min(elem[0][1], elem[1][1])
        let xEnd   = Math.max(elem[0][0], elem[1][0])
        let yEnd   = Math.max(elem[0][1], elem[1][1])

        if (xStart == xEnd || yStart == yEnd) {
            for (let y = yStart; y <= yEnd; y++) {
                for (let x = xStart; x <= xEnd; x++) {
                    grid[x + y * max] += 1
                }
            }
        }
    }))

    let overlaps = 0
    grid.forEach(val => overlaps += (val > 1) ? 1 : 0)

    console.log(`Solution 1: ${overlaps}`)
}

function solve2(data) {
    let all_vals = []
    data.replace(" ", "").replace("->", ",").split("\n").forEach(elem => {
        elem.split(",").map(s => parseInt(s)).forEach(i => all_vals.push(i))
    });

    const max = Math.max(...all_vals) + 1

    let grid = []
    for (let i = 0; i < max * max; i++) grid.push(0)

    const points = data.split("\n").map(str => str.replace(" ", "").split("->").map(arr_str => arr_str.split(",").map(s => parseInt(s))))
    
    points.forEach((elem => {
        let xStart = Math.min(elem[0][0], elem[1][0])
        let yStart = Math.min(elem[0][1], elem[1][1])
        let xEnd   = Math.max(elem[0][0], elem[1][0])
        let yEnd   = Math.max(elem[0][1], elem[1][1])

        if (xStart == xEnd || yStart == yEnd) {
            for (let y = yStart; y <= yEnd; y++) {
                for (let x = xStart; x <= xEnd; x++) {
                    grid[x + y * max] += 1
                }
            }
        } else {
            let xDiff = Math.sign(elem[1][0] - elem[0][0])
            let yDiff = Math.sign(elem[1][1] - elem[0][1])
            
            for (let i = 0; i <= Math.abs(xStart - xEnd); i++) {
                const x = elem[0][0] + i * xDiff
                const y = elem[0][1] + i * yDiff
                
                grid[x + y * max] += 1
            }
        }
    }))

    let overlaps = 0
    grid.forEach(val => overlaps += (val > 1) ? 1 : 0)

    console.log(`Solution 2: ${overlaps}`)
}

const data = fs.readFileSync("data.txt").toString()
solve1(data)
solve2(data)
