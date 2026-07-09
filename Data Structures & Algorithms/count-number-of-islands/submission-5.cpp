class Solution 
{

private:
    int res = 0;
    int ROWS;
    int COLS;

public:
    int numIslands(vector<vector<char>>& grid) 
    {
        ROWS = static_cast<int>(grid.size());
        COLS = static_cast<int>(grid[0].size());


        for (int i = 0; i < ROWS; i++)
        {
            for (int j = 0; j < COLS; j++)
            {
                if (grid[i][j] == '1')
                {
                    res++;
                    dfs(i, j, grid);

                }
            }
        }

        return res;   
    }

    void dfs(int row, int col, vector<vector<char>>& grid)
    {
        if (row < 0 || col < 0 || row == ROWS || col == COLS)
        {
            return;
        }

        if (grid[row][col] == '0') 
        {
            return;
        }

        // Then we can flip off this cell
        grid[row][col] = '0';

        dfs(row + 1, col, grid);
        dfs(row -1, col, grid);
        dfs(row, col + 1, grid);
        dfs(row, col - 1, grid);

    }
};
