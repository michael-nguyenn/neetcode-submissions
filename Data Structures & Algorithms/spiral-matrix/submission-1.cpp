class Solution 
{
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) 
    {
        std::vector<int> res{};
        int left = 0, right = static_cast<int>(matrix[0].size());
        int top = 0, bottom = static_cast<int>(matrix.size());

        while (left < right && top < bottom)
        {
            // TOP LEFT --> TOP RIGHT
            for (int i = left; i < right; i++)
            {
                res.push_back(matrix[top][i]);
            }

            // Since we've added the whole top row, we can move top down
            top++;

            // TOP RIGHT --> BOTTOM RIGHT
            for (int i = top; i < bottom; i++)
            {
                res.push_back(matrix[i][right - 1]);
            }

            // Right Column covered
            right--;

            // Another bounds check incase it's a single column or single row
            if (!(left < right && top < bottom)) { break; }

            // BOTTOM RIGHT -> BOTTOM LEFT
            for (int i = right - 1; i >= left; i--)
            {
                res.push_back(matrix[bottom-1][i]);
            }
            bottom--;

            // Finally we do BOTTOM LEFT --> TOP LEFT
            for (int i = bottom - 1; i >= top; i--)
            {
                res.push_back(matrix[i][left]);
            }
            left++;
        }

        return res;
    }
};
