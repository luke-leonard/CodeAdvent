module Main where
import System.IO 


main :: IO ()
main = do
    contents <- readFile "Days/Day02/Input.txt" 
    let strTupleList = map (tuplifyPair . words) (lines contents)
    print . tupleProduct . getResultingLocation . typecastInts $ strTupleList

tuplifyPair :: [a] -> (a,a)
tuplifyPair [x,y] = (x,y)

typecastInts :: [(String,String)] -> [(String,Int)]
typecastInts = map typecastInt xs

typecastInt :: (String,String) -> (String,Int)
typecastInt tuple = (,) (fst tuple) (readInt (snd tuple))

readInt :: String -> Int
readInt s = read s :: Int

getResultingLocation :: [(String,Int)] -> (Int, Int, Int)
getResultingLocation xs = getResultingLocationRec xs (0,0,0)

getResultingLocationRec :: [(String,Int)] -> (Int, Int, Int) -> (Int, Int, Int)
getResultingLocationRec [] tuple = tuple
getResultingLocationRec xs tuple = getResultingLocationRec (tail xs) (adjustDirection (head xs) tuple)

adjustDirection :: (String,Int) -> (Int, Int, Int) -> (Int, Int, Int)
adjustDirection (str,value) (x, y, aim)
    | str == "forward" = (,,) (x + value) (y + (value * aim)) aim
    | str == "down" = (,,) x y (aim + value)
    | str == "up" = (,,) x y (aim - value)

tupleProduct :: (Int, Int, Int) -> Int
tupleProduct (x,y,z) = x * y
