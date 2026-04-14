class Solution {
    public boolean isValidSudoku(char[][] board) {
        // Set<Character>[] rows = new HashSet[9];
        // Set<Character>[] cols = new HashSet[9];
        // Set<Character>[][] squares = new Set[3][3];

        // for (int i=0; i<9; i++) {
        //     rows[i] = new HashSet<>();
        //     cols[i] = new HashSet<>();
        // }

        // for (int r=0; r<3; r++) {
        //     for (int c=0; c<3; c++) {
        //         squares[r][c] = new HashSet<>();
        //     }
        // }

        // for (int r=0; r<9; r++) {
        //     for (int c=0; c<9; c++) {
        //         char val = board[r][c];
        //         if (val == '.') {
        //             continue;
        //         }
        //         if (rows[r].contains(val) ||
        //             cols[c].contains(val) ||
        //             squares[r/3][c/3].contains(val)) {
        //                 return false;
        //             }

        //         rows[r].add(val);
        //         cols[c].add(val);
        //         squares[r/3][c/3].add(val);
        //     }
        // }

        // return true;

        Map<Integer, Set<Character>> rows = new HashMap<>();
        Map<Integer, Set<Character>> cols = new HashMap<>();
        Map<String, Set<Character>> squares = new HashMap<>();

        for (int r=0; r<9; r++) {
            for (int c=0; c<9; c++) {
                if (board[r][c] == '.') continue;

                String squarekey = r/3 + "," + c/3;
                Character val = board[r][c];

                if (rows.computeIfAbsent(r, k-> new HashSet<>()).contains(val) ||
                    cols.computeIfAbsent(c, k-> new HashSet<>()).contains(val) ||
                    squares.computeIfAbsent(squarekey, k-> new HashSet<>()).contains(val)) {
                        return false;
                    }

                rows.get(r).add(val);
                cols.get(c).add(val);
                squares.get(squarekey).add(val);
            }
        }
        return true;
    }
}
