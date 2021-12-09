module Main where
import System.IO 
import Data.List.Split
import Debug.Trace
import Data.List
import Data.Function
import qualified Data.Map as Map  

main :: IO ()
main = do
    contents <- readFile "Days/Day08/Input.txt" 
    let entries = lines contents
    let parsedEntries = map (tuplify2 . splitOn " | ") entries
    let strs = map decodeEntry parsedEntries
    print $ sum $ map readInt strs


sToC :: String -> Char 
sToC [] = 'q'
sToC s = head s

decodeEntry :: ([String],[String]) -> String
decodeEntry info@(_,vals) = map (getValue . sort . decodeString info) vals

readInt :: String -> Int
readInt s = read s :: Int

tuplify2 :: [String] -> ([String],[String])
tuplify2 (x:y:_) = (map sort $ sortBy (compare `on` length) $ splitOn " " x, map sort $ splitOn " "y)

get1 :: ([String],[String]) -> String
get1 (val:_,_) = val

get7 :: ([String],[String]) -> String
get7 (_:val:_,_) = val

get4 :: ([String],[String]) -> String
get4 (_:_:val:_,_) = val

get8 :: ([String],[String]) -> String
get8 (vals,_) = last vals

get1478s :: ([String],[String]) -> Int
get1478s entry@(_,outputs) = length [x | x <- outputs, (/=Nothing) (Map.lookup x myMap)]
    where  myMap = Map.fromList [(get1 entry,1),(get4 entry,4),(get7 entry,7),(get8 entry,8)]

get1478sS :: ([String],[String]) -> [String]
get1478sS entry@(_,outputs) = [x | x <- outputs, (/=Nothing) (Map.lookup x myMap)]
    where  myMap = Map.fromList [(get1 entry,1),(get4 entry,4),(get7 entry,7),(get8 entry,8)]

getA :: ([String],[String]) -> Char
getA entry@(_,_) = head $ get7 entry \\ get1 entry

getB :: ([String],[String]) -> Char
getB entry@(vals,_) = head . head $ filter ((==6) . length) (group $ sort $ concat vals)

getC :: ([String],[String]) -> Char
getC entry@(_,_) = head $ get1 entry \\ [getF entry]

getD :: ([String],[String]) -> Char
getD entry@(_,_) = head $ (get4 entry \\ get1 entry) \\ [getB entry]

getE :: ([String],[String]) -> Char
getE entry@(vals,_) = head . head $ filter ((==4) . length) (group $ sort $ concat vals)

getF :: ([String],[String]) -> Char
getF entry@(vals,_) = head . head $ filter ((==9) . length) (group $ sort $ concat vals)

getG :: ([String],[String]) -> Char
getG entry@(_,_) = head $ (get8 entry \\ (get7 entry `union` get4 entry)) \\ [getE entry]

getValue :: String -> Char
getValue "abcefg" = '0'
getValue "cf" = '1'
getValue "acdeg" = '2'
getValue "acdfg" = '3'
getValue "bcdf" = '4'
getValue "abdfg" = '5'
getValue "abdefg" = '6'
getValue "acf" = '7'
getValue "abcdefg" = '8'
getValue "abcdfg" = '9'
getValue x = trace x (head x)

decodeChar :: ([String],[String]) -> Char -> Char
decodeChar info 'a' = getA info
decodeChar info 'b' = getB info
decodeChar info 'c' = getC info
decodeChar info 'd' = getD info
decodeChar info 'e' = getE info
decodeChar info 'f' = getF info
decodeChar info 'g' = getG info
decodeChar info x = getA info


decodeString :: ([String],[String])-> String -> String
decodeString info = map (decodeCharInv info)


decodeCharInv :: ([String],[String]) -> Char -> Char
decodeCharInv info char 
    | char == getA info = 'a'
    | char == getB info = 'b'
    | char == getC info = 'c'
    | char == getD info = 'd'
    | char == getE info = 'e'
    | char == getF info = 'f'
    | char == getG info = 'g'
    | otherwise = 'a'
