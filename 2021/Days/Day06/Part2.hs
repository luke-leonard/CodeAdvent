module Main where
import System.IO 
import Data.List.Split
import Debug.Trace
import Data.List



main :: IO ()
main = do
    contents <- readFile "Days/Day06/Input.txt" 
    let starterFish = map readInt (splitOn "," contents)
    let fishCounts = initFishList starterFish
    print fishCounts
    print . sum $ getFishCount fishCounts 256


readInt :: String -> Int
readInt s = read s :: Int

initFishList :: [Int] -> [Int]
initFishList fish = map (fishAtDay fish) [0..8]

fishAtDay :: [Int] -> Int -> Int
fishAtDay fish day = length [x | x <- fish, x == day]

getFishCount :: [Int] -> Int -> [Int] 
getFishCount currentFish day
    | day == 0 = currentFish
    | otherwise = getFishCount (take 6 (tail currentFish) ++ [currentFish !! 7 + head currentFish] ++ [currentFish !! 8] ++ [head currentFish]) (day - 1)