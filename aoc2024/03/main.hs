import Data.List
import Debug.Trace
import Control.Monad
import Data.Maybe

filename = "data.txt"  
-- filename = "test.txt"

type PairInt = (Int, Int)

unwrap :: Maybe a -> a
unwrap Nothing = error "This cannot happen"
unwrap (Just x) = x

findSubstring :: String -> String -> Maybe Int
findSubstring needle haystack = findIndex (isPrefixOf needle) (tails haystack)

take_substr :: Int -> String -> String
take_substr n str = drop n str

parse_sym :: String -> Char -> Maybe ()
parse_sym [] _ = Nothing
parse_sym (x:xs) c
  | x == c = Just ()
  | otherwise = Nothing

isNumeric :: Char -> Bool
isNumeric c
  | c == '0' || c == '1' || c == '2' || c == '3' || c == '4' || c == '5' || c == '6' || c == '7' || c == '8' || c == '9' = True
  | otherwise = False

parse_number :: String -> Maybe PairInt 
parse_number [] = Nothing
parse_number str
  | length a == 0 = Nothing
  | otherwise = Just (read a, length a)
  where
    a = takeWhile isNumeric str

parse_next :: String -> Maybe Int -> Maybe (Int, PairInt) 
parse_next substr Nothing = Nothing
parse_next substr (Just start) = do
  let n = start + 4
  (x, len_x) <- parse_number $ take_substr n substr
  _ <- parse_sym (take_substr (n + len_x) substr) ','
  (y, len_y) <- parse_number $ take_substr (n + len_x + 1) substr
  _ <- parse_sym (take_substr (n + len_x + len_y + 1) substr) ')'
  return ((n+len_x+len_y+1), (x, y))

sol1 :: String -> Int -> [PairInt] -> [PairInt]
sol1 content pos acc
  | (length content) < pos = acc
  | isNothing a = sol1 content (pos+4) acc
  | isJust a = sol1 content (pos+n) (acc ++ [vals])
    where
      a = parse_next s (findSubstring "mul(" s)
      s = take_substr pos content
      n = fst $ unwrap a
      vals = snd $ unwrap a

sol2 = 0

main :: IO ()
main = do
  contents <- readFile filename
  putStrLn $ "Solution 1: " ++ (show $ foldl (\acc (x, y) -> acc + (x * y)) 0 (sol1 contents 0 []))
  putStrLn $ "Solution 2: " ++ (show $ sol2)
  return ()
