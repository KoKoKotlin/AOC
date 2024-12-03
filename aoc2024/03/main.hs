import Data.List
import Data.Ord
import Debug.Trace
import Control.Monad
import Data.Maybe

filename = "data.txt"  
-- filename = "test.txt"

type PairInt = (Int, Int)

data TokenType = Do | Dont | Mul
instance Show TokenType where
  show Do = "Do"
  show Dont = "Dont"
  show Mul = "Mul"
instance Eq TokenType where
  (==) :: TokenType -> TokenType -> Bool
  Do == Do = True
  Do == Dont = False
  Do == Mul = False
  Dont == Do = False
  Dont == Dont = True
  Dont == Mul = False
  Mul == Do = False
  Mul == Dont = False
  Mul == Mul = True

unwrap :: Maybe a -> a
unwrap Nothing = error "This cannot happen"
unwrap (Just x) = x

findSubstring :: String -> String -> Maybe Int
findSubstring needle haystack = findIndex (isPrefixOf needle) (tails haystack)

findNext :: String -> Maybe (TokenType, Int)
findNext str
  | (length list) == 0 = Nothing
  | otherwise = Just (minimumBy (comparing snd) list)
  where
    list = map (\(a, b) -> (a, unwrap b)) $ filter (\(_, b) -> isJust b) [a,b,c]
    a = (Mul, findSubstring "mul(" str)
    b = (Do, findSubstring "do()" str)
    c = (Dont, findSubstring "don't()" str)

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

sol2 :: String -> Bool -> Int -> [PairInt] -> [PairInt]
sol2 content active pos acc
  | (length content) < pos = acc
  | isNothing b = acc
  | isJust b && ttype == Do = sol2 content True (pos+offset+4) acc
  | isJust b && ttype == Dont = sol2 content False (pos+offset+7) acc 
  | isJust b && ttype == Mul && isJust a = sol2 content active (pos+len) acc_mod
  | isJust b && ttype == Mul && isNothing a = sol2 content active (pos+offset+4) acc
    where
      b = findNext s
      offset = (snd . unwrap) b
      ttype = (fst . unwrap) b
      a = parse_next s (Just offset)
      len = (fst . unwrap) a
      val = (snd . unwrap) a
      s = take_substr pos content
      acc_mod = if active then acc ++ [val] else acc

main :: IO ()
main = do
  contents <- readFile filename
  putStrLn $ "Solution 1: " ++ (show $ foldl (\acc (x, y) -> acc + (x * y)) 0 (sol1 contents 0 []))
  putStrLn $ "Solution 2: " ++ (show $ foldl (\acc (x, y) -> acc + (x * y)) 0 (sol2 contents True 0 []))
  return ()
