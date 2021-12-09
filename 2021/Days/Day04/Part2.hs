module Main where
import System.IO 
import Data.List.Split
import Debug.Trace

flag = -1

main :: IO ()
main = do
    contents <- readFile "Days/Day04/Input.txt" 
    let contentList = splitOn "\n\n" contents
    let calls = map readInt (splitOn "," (head contentList))
    let boards = map splitBoard (tail contentList)
    print . getWinningScore $ getWinningBoard boards calls


splitBoard :: String -> [[Int]]
splitBoard str = map (filter (>= 0) . map readInt . splitOn " ") (splitOn "\n" str)

readInt :: String -> Int
readInt "" = flag
readInt s = read s :: Int

getWinningScore :: ((Int,Int),[[Int]]) -> Int
getWinningScore ((val,index),board) = sum ( map (foldl addIfRemaining 0) board) * val

addIfRemaining :: Int -> Int -> Int
addIfRemaining current numToAdd
    | numToAdd == flag = current
    | otherwise = numToAdd + current

getWinningBoard :: [[[Int]]] -> [Int] -> ((Int,Int),[[Int]])
getWinningBoard boards nums = getMaxBoardRec ((0,flag),[]) (map (`determineRoundStart` nums) boards)

getMaxBoardRec :: ((Int,Int),[[Int]]) -> [((Int,Int),[[Int]])] -> ((Int,Int),[[Int]])
getMaxBoardRec board [] = board
getMaxBoardRec board1 (board2:boards) 
    | (snd . fst $ board1 ) > (snd . fst $ board2) = getMaxBoardRec board1 boards
    | otherwise = getMaxBoardRec board2 boards

determineRoundStart :: [[Int]] -> [Int] -> ((Int,Int),[[Int]])
determineRoundStart board nums = determineRound (applyNumberToBoard board (head nums)) nums 0

determineRound :: [[Int]] -> [Int] -> Int -> ((Int,Int),[[Int]])
determineRound board [] itt = ((flag, itt),board)
determineRound board nums itt
    | checkForWin board = ((head nums, itt), board)
    | otherwise = determineRound (applyNumberToBoard board (head . tail $ nums)) (tail nums) (itt + 1)

applyNumberToBoard :: [[Int]] -> Int -> [[Int]]
applyNumberToBoard board numberToCheck = map ( map (markNumber numberToCheck)) board

markNumber :: Int -> Int -> Int
markNumber check val
    | val == check = flag
    | otherwise = val

checkForWin :: [[Int]] -> Bool 
checkForWin board = checkRowsForWin board || checkColsForWin board

checkRowsForWin :: [[Int]] -> Bool
checkRowsForWin [] = False
checkRowsForWin board
    | checkRowForWin . head $ board = True 
    | otherwise = checkRowsForWin . tail $ board

checkRowForWin :: [Int] -> Bool 
checkRowForWin [] = True 
checkRowForWin row 
    | head row == flag = checkRowForWin . tail $ row
    | otherwise = False 

checkColsForWin :: [[Int]] -> Bool
checkColsForWin ([]:xs) = False
checkColsForWin board
    | checkColForWin [head x | x <- board] = True
    | otherwise = checkColsForWin [tail x | x <- board] 

checkColForWin :: [Int] -> Bool
checkColForWin [] = True 
checkColForWin col
    | head col == flag = checkColForWin (tail col)
    | otherwise = False 