import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

public class Main {

    public static List<String> loadData() {
        List<String> lines = null;

        try {
            BufferedReader bReader = Files.newBufferedReader(Paths.get("data.txt"));
            lines = bReader.lines().collect(Collectors.toList());
        } catch (IOException e) { }
        
        if (lines == null) throw new IllegalStateException("Couldn't load data!");

        return lines;
    }

    public static void solve1(List<String> lines) {
        int x = 0, y = 0;
        for (var line: lines) {
            String parts[] = line.split(" ");
            switch (parts[0]) {
                case "forward":
                    x += Integer.valueOf(parts[1]);
                    break;
                case "down":
                case "up":
                    y += ((parts[0].equals("down")) ? 1 : -1) * Integer.valueOf(parts[1]);
                    break;
            }
        }

        System.out.printf("Solution 1: %d\n", x * y);
    }

    public static void solve2(List<String> lines) {
        int x = 0, y = 0, aim = 0;
        for (var line: lines) {
            String parts[] = line.split(" ");
            switch (parts[0]) {
                case "forward":
                    x += Integer.valueOf(parts[1]);
                    y += Integer.valueOf(parts[1]) * aim;
                    break;
                case "down":
                case "up":
                    aim += ((parts[0].equals("down")) ? 1 : -1) * Integer.valueOf(parts[1]);
                    break;
            }
        }

        System.out.printf("Solution 2: %d\n", x * y);
    }
    
    public static void main(String[] args) {
        List<String> lines = loadData();
        solve1(lines);
        solve2(lines);
    }
}