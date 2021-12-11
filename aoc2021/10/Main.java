import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.List;
import java.util.stream.Collectors;

public class Main {

    public static List<String> loadData() {
        List<String> lines = null;

        try {
            BufferedReader bReader = Files.newBufferedReader(Paths.get("test.txt"));
            lines = bReader.lines().collect(Collectors.toList());
        } catch (IOException e) { }
        
        if (lines == null) throw new IllegalStateException("Couldn't load data!");

        return lines;
    }

    public static int syntaxScore(String symbol) {
        switch (symbol) {
            case "(", ")" -> { return 3; }
            case "[", "]" -> { return 57; }
            case "{", "}" -> { return 1197; }
            case "<", ">" -> { return 25137; }
        }

        throw new IllegalArgumentException("Symbol not found!");
    }

    public static void solve1(List<String> lines) {
        Deque<String> stack = new ArrayDeque<>();
        int score = 0;
        for (String line : lines) {
            for (String symbol : line.split("")) {
                switch(symbol) {
                    case "(", "[", "{", "<" -> {
                        stack.push(symbol);
                    }

                    case ")", "]", "}", ">" -> {
                        String symbol2 = stack.pop();

                        if (!(symbol.equals(")") && symbol2.equals("(") ||
                            symbol.equals("]") && symbol2.equals("[") ||
                            symbol.equals("}") && symbol2.equals("{") ||
                            symbol.equals(">") && symbol2.equals("<"))) {
                                score += syntaxScore(symbol);
                                break;
                            }
                    }
                }
            }
        }

        System.out.printf("Solution 1: %d\n", score);
    }

    public static void solve2(List<String> lines) {
        Deque<String> stack = new ArrayDeque<>();

        List<Integer> scores = new ArrayList<>();
        for (String line : lines) {
            boolean isCorrupted = false;
            for (String symbol : line.split("")) {
                switch(symbol) {
                    case "(", "[", "{", "<" -> {
                        stack.push(symbol);
                    }

                    case ")", "]", "}", ">" -> {
                        String symbol2 = stack.pop();

                        if (!(symbol.equals(")") && symbol2.equals("(") ||
                            symbol.equals("]") && symbol2.equals("[") ||
                            symbol.equals("}") && symbol2.equals("{") ||
                            symbol.equals(">") && symbol2.equals("<"))) {
                                isCorrupted = true;
                                break;
                            }
                    }
                }
            }

            if (!isCorrupted) {
                int score = 0;
                System.out.printf("Stack size: %d\n", stack.size());
                while (!stack.isEmpty()) {
                    String symbol = stack.pop();
                    System.out.print(symbol);
                    score *= 5;
                    switch (symbol) {
                        case "(" -> { score += 1; }
                        case "[" -> { score += 2; }
                        case "{" -> { score += 3; }
                        case "<" -> { score += 4; }
                        default -> { throw new IllegalStateException("Symbol not found!"); }
                    }
                }

                scores.add(score);
                System.out.println("\n" + score);
            }
        }


        scores.sort((i1, i2) -> {
            return (i1 < i2) ? i1 : i2;
        });
        System.out.printf("Solution 2: %d\n", scores.get(scores.size() / 2 + 1));
    }
    
    public static void main(String[] args) {
        List<String> lines = loadData();
        solve1(lines);
        solve2(lines);
    }
}