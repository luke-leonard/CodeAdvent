module Main where
import System.IO 
import Data.List.Split
import Debug.Trace
import Data.List



main :: IO ()
main = do
    contents <- readFile "Days/Day07/Input.txt" 
    let startingPositions = map readInt (splitOn "," contents)
    let mappedCrabs = getMappedArray startingPositions
    let forwardMap = getFuelCostArr mappedCrabs 0 0 0
    let backwardsMap = getFuelCostArr (reverse mappedCrabs) 0 0 0
    print . minimum $ zipWith (+) forwardMap (reverse backwardsMap)

readInt :: String -> Int
readInt s = read s :: Int

getFuelCostArr :: [(Int,Int)] -> Int -> Int -> Int-> [Int]
getFuelCostArr [] _ _ _ = []
getFuelCostArr ((position,crabCount):crabs) amountOfFuelNeeded fuelIncreaseRate numCrabs = amountOfFuelNeeded : getFuelCostArr crabs (amountOfFuelNeeded + fuelIncreaseRate + numCrabs + crabCount) (fuelIncreaseRate + numCrabs + crabCount) (numCrabs + crabCount)

getMappedArray:: [Int] -> [(Int,Int)]
getMappedArray crabs = map (crabsAtPos crabs) [(minimum crabs)..(maximum crabs)]

crabsAtPos :: [Int] -> Int -> (Int,Int)
crabsAtPos crabs day = (day,length [x | x <- crabs, x == day])




