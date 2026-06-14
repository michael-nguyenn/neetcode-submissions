class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) 
    {
        std::array<std::unordered_set<int>, 9> rows{}, cols{}, boxes{};

        for (int i = 0; i < 9; i++)
        {
            for (int j = 0; j < 9; j++)
            {
                if (board[i][j] == '.')
                {
                    continue;
                }

                int cur_num = board[i][j];
                int box_idx = (i / 3) * 3 + (j / 3);
                
                if (rows[i].contains(cur_num) || 
                    cols[j].contains(cur_num) || 
                    boxes[box_idx].contains(cur_num))
                    {
                        return false;
                    }

                rows[i].insert(cur_num);
                cols[j].insert(cur_num);
                boxes[box_idx].insert(cur_num);
            }
        }
        return true; 
    }
};
