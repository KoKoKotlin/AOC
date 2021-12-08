import java.nio.file.Files
import java.nio.file.Paths

fun load_data(): List<String> {
    val bReader = Files.newBufferedReader(Paths.get("data.txt"))
    
    return bReader.readLines()
}

fun solve1(data: List<String>) {
    var nums = data[0].split(",").map { it.toInt() }.toList()

    repeat(80) {
        val nextDay = mutableListOf<Int>()
        for (i in nums.indices) {
            val num = nums[i]

            when(num) {
                0 -> {
                    nextDay.addAll(listOf(6, 8))
                }
                else -> {
                    nextDay.add(num - 1)
                }
            }
        }

        nums = nextDay
    }
    
    println("Solution 1: ${nums.size}")
}

const val NUMBER_OF_DAYS: Int = 256

// table with number of fish at index i
fun solve2(data: List<String>) {
    var nums = data[0].split(",").map { it.toInt() }.toList()
    var table = Array(9) { i ->
        nums.filter { it == i }.size.toLong()
    }

    repeat(NUMBER_OF_DAYS) { 
        val newTable = Array(9) { 0L }
        for (i in 0 until table.size) {    
            when(i) {   
                0 -> {
                    newTable[8] = table[0]
                    newTable[6] = table[0]
                }
                else -> newTable[i - 1] += table[i]
            }
        }

        table = newTable
    }

    println("Solution 2: ${table.toList().sum()}")
}

fun main() {
    val data = load_data()
    solve1(data)
    solve2(data)
}