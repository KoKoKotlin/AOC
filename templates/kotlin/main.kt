
import java.nio.file.Files
import java.nio.file.Paths

fun load_data(): List<String> {
    val bReader = Files.newBufferedReader(Paths.get("data.txt"))
    
    return bReader.readLines()
}

fun solve1(data: List<String>) {
    println("Solution 1: ${0}")
}

fun solve2(data: List<String>) {
    println("Solution 2: ${0}")
}

fun main() {
    val data = load_data()
    solve1(data)
    solve2(data)
}