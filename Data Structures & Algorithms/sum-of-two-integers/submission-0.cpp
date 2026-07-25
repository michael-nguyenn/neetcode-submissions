// Binary Addition
// 0 + 0 = 0
// 0 + 1 = 1
// 1 + 0 = 1
// 1 + 1 = 0 with a carry over
// Using the XOR operator will give us the desired results except it doesn't account
// for the carry over in 1 + 1 
// To determine the carry over we could use AND and left shift by one

class Solution 
{
public:
    int getSum(int a, int b) 
    {
        while (b != 0)
        {
            int carry = (a & b) << 1;
            a = a ^ b;
            b = carry;
        }

        return a;
    }
};
