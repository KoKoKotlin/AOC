import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
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
        int score = 0;
        for (String line : lines) {
            Deque<String> stack = new ArrayDeque<>();
            for (String symbol : line.split("")) {
                switch(symbol) {
                    case "(", "[", "{", "<" -> {
                        stack.addFirst(symbol);
                    }

                    case ")", "]", "}", ">" -> {
                        String symbol2 = stack.removeFirst();

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
        List<Long> scores = new ArrayList<>();

        for (String line : lines) {
            Deque<Character> stack = new LinkedList<>();
            boolean isCorrupted = false;
            inner: for (int i = 0; i < line.length(); i++) {
                char symbol = line.charAt(i);
                switch(symbol) {
                    case '(', '[', '{', '<' -> {
                        stack.addFirst(symbol);
                    }

                    default -> {
                        char symbol2 = stack.removeFirst();

                        if (!(symbol == ')' && symbol2 == '(' ||
                              symbol == ']' && symbol2 == '[' ||
                              symbol == '}' && symbol2 == '{' ||
                              symbol == '>' && symbol2 == '<')) {
                            isCorrupted = true;
                            break inner;
                        }
                    }
                }
            }

            if (!isCorrupted) {
                long score = 0;
                while (!stack.isEmpty()) {
                    char symbol = stack.removeFirst();
                    score *= 5L;
                    switch (symbol) {
                        case '(' -> { score += 1L; }
                        case '[' -> { score += 2L; }
                        case '{' -> { score += 3L; }
                        case '<' -> { score += 4L; }
                        default -> { throw new IllegalStateException("Symbol not found!"); }
                    }
                }
                scores.add(score);
            }
        }


        scores.sort((i1, i2) -> {
            if (i1 < i2) return -1;
            else if (i1 > i2) return 1;
            else return 0;
        });
        System.out.printf("Solution 2: %d\n", scores.get(scores.size() / 2));
    }
    
    public static void main(String[] args) {
        List<String> lines = loadData();
        solve1(lines);
        solve2(lines);
    }
}