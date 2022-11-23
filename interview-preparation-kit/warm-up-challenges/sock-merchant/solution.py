# https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

def sockMerchant(n, ar):
    if (0 < n and n < 101):
        if (len(ar) > 0 or len(ar) == 1) and (len(ar)-1 < n):
            total_pairs = 0
            colors = []
            
            for i in ar:
                if i in colors:
                    colors.remove(i)
                    total_pairs += 1;
                else:
                    colors.append(i)
            return total_pairs
        
n = int(input().strip())
ar = list(map(int, input().rstrip().split()))

result = sockMerchant(n, ar)
print(result)