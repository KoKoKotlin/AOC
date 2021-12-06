import java.nio.file.Files
import java.nio.file.Paths

fun load_data(): List<String> {
    val bReader = Files.newBufferedReader(Paths.get("data.txt"))
    
    return bReader.readLines()
}

class Board(val nums: List<Int>) {
    val drawNums = mutableListOf<Int>()
    val rows: List<List<Int>>
    val cols: List<List<Int>>
    
    init {
        rows = List(5) { nums.subList(it * 5, (it + 1) * 5) }
        cols = List(5) { listOf(nums[it + 0 * 5], nums[it + 1 * 5], nums[it + 2 * 5], nums[it + 3 * 5], nums[it + 4 * 5]) }
    }

    fun hasWon() = 
        cols.any { drawNums.containsAll(it) }
    ||  rows.any { drawNums.containsAll(it) }

    fun calcRes(num: Int) = num * (nums.filter { it !in drawNums } .sum())
}

fun solve1(data: List<String>) {
    val nums = data[0].split(",").map { it.toInt() }
    
    val boards = data.subList(1, data.size).filter { !it.isBlank() }.chunked(5)                                                                 // initial parsing
                                      .map { list -> list.map { str -> str.split(" ").filter { !it.isBlank() }.map { it.toInt() } }.flatten() } // creating nums for boards
                                      .map { Board(it) }                                                                                        // creating the actual boards
                                      
    for (num in nums) {
        boards.forEach { it.drawNums.add(num) }
        val winners = boards.filter { it.hasWon() }

        if (winners.size > 0) {
            println("Solution 1: ${ winners[0].calcRes(num) }")
            break
        }    
    }
}

fun solve2(data: List<String>) {
    val nums = data[0].split(",").map { it.toInt() }
    
    var boards = data.subList(1, data.size).filter { !it.isBlank() }.chunked(5)                                                                 // initial parsing
                                      .map { list -> list.map { str -> str.split(" ").filter { !it.isBlank() }.map { it.toInt() } }.flatten() } // creating nums for boards
                                      .map { Board(it) }                                                                                        // creating the actual boards
                                      
    for (num in nums) {
        boards.forEach { it.drawNums.add(num) }
        boards = boards.filter { !it.hasWon() || boards.size == 1 }

        if (boards.size == 1 && boards[0].hasWon()) {
            println("Solution 2: ${ boards[0].calcRes(num) }")
            break
        }
    }
}

fun main() {
    val data = load_data()
    solve1(data)
    solve2(data)
}