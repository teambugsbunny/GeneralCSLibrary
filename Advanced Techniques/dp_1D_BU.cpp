vector <int> abc;
int states[4001];

int dp(int ribbon) {

    if (ribbon == 0)
        return 0;
    
    if (ribbon<0)
        return -10000;

    if (states[ribbon] != -1)
        return states[ribbon];
    
    return states[ribbon] = MAX(1 + dp(ribbon - abc[1]), 1 + dp(ribbon - abc[0]), 1 + dp(ribbon - abc[2]));
}
