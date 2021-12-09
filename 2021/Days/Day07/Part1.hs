module Main where
import System.IO 
import Data.List.Split
import Debug.Trace
import Data.List



main :: IO ()
main = do
    contents <- readFile "Days/Day07/Input.txt" 
    let startingPositions = sort (map readInt (splitOn "," contents))
    let halfLength = length startingPositions `div` 2
    let firstHalf = take halfLength startingPositions
    let secondHalf = take halfLength (reverse startingPositions)
    print (getFuelCost firstHalf secondHalf)

readInt :: String -> Int
readInt s = read s :: Int

getFuelCost :: [Int] -> [Int] -> Int 
getFuelCost smaller larger = sum (zipWith (-) larger smaller)