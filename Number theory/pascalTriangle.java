        int T, N;
        T = scanner.nextInt();
        for (int i = 0; i < T; i++) {
            N = scanner.nextInt();
            BigInteger c = BigInteger.ONE;
            for (int j = 1; j < N + 2; j++) {
                System.out.print(c.mod(BigInteger.valueOf(1000000000)) + " ");
                c = c.multiply(BigInteger.valueOf(N + 1 - j));
                c = c.divide(BigInteger.valueOf(j));
            }
            System.out.println();
        }

