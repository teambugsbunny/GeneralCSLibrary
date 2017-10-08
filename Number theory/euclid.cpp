//For System of two equation use Cramer's rule
int x, y, d;
void extendedEuclid(int a, int b) {
if (b == 0) { 
x = 1; 
y = 0; 
d = a; 
return; 
}
extendedEuclid(b, a % b);
int x1 = y;
int y1 = x - (a / b) * y;
x = x1;
y = y1;
}


//main
    extendedEuclid(n1, n2);
    bool failed = false;
    
    if (n % d) 
        failed = true;
    else {
        x *= (n / d);
        y *= (n / d);
        ll aDivider = n2 / d;
        ll bDivider = n1 / d;
        ll lowerBound = (ll) ceil(-x / (double) aDivider);
        ll upperBound = (ll) floor(y / (double) bDivider);

        if (lowerBound > upperBound) failed = true;

        else {
            if ( (x + aDivider * lowerBound) + (y - bDivider * lowerBound) < (x + aDivider * upperBound) + (y - bDivider * upperBound) )
                x += aDivider * lowerBound, y -= bDivider * lowerBound;
            else
                x += aDivider * upperBound, y -= bDivider * upperBound;
        }
    }

    if (failed) puts("failed");
    else printf("%lld %lld\n", x, y);

