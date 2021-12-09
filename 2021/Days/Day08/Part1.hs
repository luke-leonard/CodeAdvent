module Main where
import System.IO 
import Data.List.Split
import Debug.Trace
import Data.List
import Data.Function
import qualified Data.Map as Map  

data Mapping = Mapping { 
    zero :: String,
    one :: String,
    two :: String,
    three :: String,
    four :: String,
    five :: String,
    six :: String,
    seven :: String,
    eight :: String,
    nine :: String
}


main :: IO ()
main = do
    contents <- readFile "Days/Day08/Input.txt" 
    let entries = lines contents
    let parsedEntries = map (tuplify2 . splitOn " | ") entries
    let numOf = sum $ map get1478s parsedEntries
    print numOf

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