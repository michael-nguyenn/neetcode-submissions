class Solution 
{
public:
    bool isValid(const string& s) 
    {
        // need a stack to store opening brackets
        std::stack<char> opening_s{};

        // need a map: closing -> opening
        // then once we run into a closing bracket, we can use that as an index
        // and see if that matches the opening bracket we have stored in our stack
        std::unordered_map<char, char> brackets{};
        brackets['}'] = '{';
        brackets[']'] = '[';
        brackets[')'] = '(';

        for (char c : s)
        {
            // if it's an opening brace we add it to our stack
            if (c == '{' || c == '(' || c == '[') { opening_s.push(c); }

            // once we encounter a closing brace we'll pop our stack
            // and compare it to see if it matches the closing brace
            else 
            {
                // if our stack is empty, then we have too many opening braces
                if (opening_s.empty()) { return false; }

                char opening_brace = opening_s.top();
                opening_s.pop();

                // here we're getting our opening brace, and then we're using the
                // closing brace to map brackets to its matching opening brace
                if (opening_brace != brackets[c]) { return false; }

            }
        }

        // once we're out of here we need to make sure our stack is empty
        return opening_s.empty();
        
    }
};
