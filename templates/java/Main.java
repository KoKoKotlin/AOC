package templates.java;

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

    }

    public static void solve2(List<String> lines) {

    }
    
    public static void main(String[] args) {
        List<String> lines = loadData();
        solve1(lines);
        solve2(lines);
    }
}