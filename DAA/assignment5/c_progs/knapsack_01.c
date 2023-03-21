// Solve the following instances of the 0/1 Knapsack problem given the Knapsack capacity W=7
// Item  Weight  Value
// 1     3       10
// 2     2       12

#include <stdio.h>
#include <string.h>

struct Item
{
    int weight, value;
};

int knapSack(int W, struct Item arr[], int n)
{
    int dp[W + 1];
    memset(dp, 0, sizeof(dp));
    for (int i = 1; i < n + 1; i++)
    {
        for (int w = W; w >= 0; w--)
        {
            if (arr[i - 1].weight <= w)
                dp[w] = (dp[w] > (dp[w - arr[i - 1].weight] + arr[i - 1].value)) ? dp[w] : (dp[w - arr[i - 1].weight] + arr[i - 1].value);
        }
    }
    return dp[W];
}

int main()
{
    struct Item arr[] = {{3, 10}, {2, 12}};
    int W = 7;
    int n = sizeof(arr) / sizeof(struct Item);
    printf("0/1 Knapsack problem in C\n");
    printf("Knapsack Capacity: %d\n", W);
    printf("Item\tWeight\tValue\n");
    for (int i = 0; i < n; i++)
        printf("%d \t%d \t%d \n", i + 1, arr[i].weight, arr[i].value);
    printf("Maximum profit: %d\n", knapSack(W, arr, n));
    return 0;
}

// OUTPUT
// 0/1 Knapsack problem in C
// Knapsack Capacity: 7
// Item    Weight  Value
// 1       3       10
// 2       2       12
// Maximum profit: 22