
-- filename = "test.txt"
filename = "data.txt"

parseLines :: String -> [[Int]]
parseLines contents = map (\l -> map read l) $ map words (lines contents)

dropLast :: [a] -> [a]
dropLast [] = []
dropLast [x] = []
dropLast lst = (reverse . tail . reverse) lst 

removeNth :: Int -> [a] -> [a]
removeNth n xs =
    let (before, after) = splitAt n xs
    in before ++ drop 1 after

checkSave :: [Int] -> Bool
checkSave lst = (all (\x -> (1 <= (abs x)) && ((abs x) <= 3)) diffs) && ((all (< 0) diffs) || (all (> 0) diffs))
  where
    diffs = map (\(x, y) -> x - y) $ zip (dropLast lst) (tail lst)

checkSave2 :: Int -> [Int] -> Bool
checkSave2 n lst
  | n >= length lst = False
  | otherwise = if (checkSave $ removeNth n lst) then True else checkSave2 (n+1) lst

sol1 :: [[Int]] -> Int
sol1 lists = length $ filter checkSave lists 

sol2 :: [[Int]] -> Int
sol2 lists = length $ filter (checkSave2 0) lists
  
main :: IO ()
main = do 
  contents <- readFile filename
  let lists = parseLines contents
  putStrLn $ "Solution 1: " ++ (show $ sol1 lists)
  putStrLn $ "Solution 2: " ++ (show $ sol2 lists)
  return ()
