class Soltuion{
public:
  int longestVaildParentheses(string s){
    // 1 is (, -1 is), 2,4,6,8.. denote the length of a
    // legal substring with valid parentheses
    vector<int> stack;
    for (int i = 0; i < s.length(); i++){
      if(s[i] =='('){
        stack.push_back(1);
      }else{
        if (stack.size() > 0 && stack[stack.size() -1] == 1){
          stack[]
        }
      }
    }
  }
}
