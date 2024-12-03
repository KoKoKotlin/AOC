import Data.List

filename = "data.txt"
-- filename = "test.txt"

parse_line :: String -> [Int]
parse_line line = map read $ words line

sol1 lines = foldl (\acc (x, y) -> acc + abs (x - y)) 0 (zip (sort first_lst) (sort second_lst))
  where
    first_lst = map (head . parse_line) $ lines 
    second_lst = map (head . tail . parse_line) $ lines

count :: Int -> Int -> [Int] -> Int
count needle acc [] = acc
count needle acc (x:xs)
  | x == needle = count needle (acc + 1) xs
  | otherwise = count needle acc xs

sol2 lines = foldl (\acc x -> acc + x * (count x 0 second_lst)) 0 first_lst 
  where
    first_lst = map (head . parse_line) $ lines 
    second_lst = map (head . tail . parse_line) $ lines

main :: IO ()
main = do
  contents <- readFile filename
  putStrLn $ "Solution 1: " ++ ((show . sol1 . lines) contents)
  putStrLn $ "Solution 2: " ++ ((show . sol2 . lines) contents)
  return ()
  
  
