class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) 
    {
        std::array<std::unordered_set<char>, 9> rows{}, cols{}, boxes{};

        for (int i = 0; i < 9; i++)
        {
            for (int j = 0; j < 9; j++)
            {
                if (board[i][j] == '.')
                {
                    continue;
                }

                char cur_grid = board[i][j];
                int box_idx = (i / 3) * 3 + (j / 3);
                
                if (rows[i].contains(cur_grid) || 
                    cols[j].contains(cur_grid) || 
                    boxes[box_idx].contains(cur_grid))
                    {
                        return false;
                    }

                rows[i].insert(cur_grid);
                cols[j].insert(cur_grid);
                boxes[box_idx].insert(cur_grid);
            }
        }
        return true; 
    }
};
