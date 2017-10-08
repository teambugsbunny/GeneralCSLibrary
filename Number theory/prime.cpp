ll _sieve_size;
bitset<10000010> bs;
vi primes;
void sieve(ll upperbound) {
    _sieve_size = upperbound + 1;
    bs.set();
    bs[0] = bs[1] = 0;
    for (ll i = 2; i <= _sieve_size; i++)
        if (bs[i]) {
            for (ll j = i * i; j <= _sieve_size; j += i)
                bs[j] = 0;
            primes.push_back((int) i);
        }
}
// call this method in main method

bool primeTest(ll N) {
    if (N <= _sieve_size) 
        return bs[N];

    for (int i = 0; i < (int) primes.size(); i++)
        if (N % primes[i] == 0) 
            return false;
    return true;
}

vi primeFactors(ll N) {
    vi factors;
    ll PF_idx = 0, PF = primes[PF_idx];
    while (PF * PF <= N) {
        while (N % PF == 0) {
            N /= PF;
            factors.push_back(PF);
        }
        PF = primes[++PF_idx];
    }
    
    if (N != 1) 
        factors.push_back(N);
    
    return factors;
}


ll numPF(ll N) {
ll PF_idx = 0, PF = primes[PF_idx], ans = 0;
while (PF * PF <= N) {
while (N % PF == 0) { N /= PF; ans++; }
PF = primes[++PF_idx];
}
if (N != 1) ans++;
return ans;
}

ll numDiv(ll N) {
ll PF_idx = 0, PF = primes[PF_idx], ans = 1;
// start from ans = 1
while (PF * PF <= N) {
ll power = 0;
// count the power
while (N % PF == 0) { N /= PF; power++; }
ans *= (power + 1);
// according to the formula
PF = primes[++PF_idx];
}
if (N != 1) ans *= 2;
// (last factor has pow = 1, we add 1 to it)
return ans;
}

ll sumDiv(ll N) {
ll PF_idx = 0, PF = primes[PF_idx], ans = 1;
// start from ans = 1
while (PF * PF <= N) {
ll power = 0;
while (N % PF == 0) { N /= PF; power++; }
ans *= ((ll)pow((double)PF, power + 1.0) - 1) / (PF - 1);
PF = primes[++PF_idx];
}
if (N != 1) ans *= ((ll)pow((double)N, 2.0) - 1) / (N - 1); // last
return ans;
}


