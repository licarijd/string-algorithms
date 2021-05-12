
// This code only contains search() and main. To complete it, see https://ide.geeksforgeeks.org/oY7OkD
 
// A suffix array based search function to search a given pattern
// 'pat' in text 'txt' using suffix array suffArr[]
void search(char *pat, char *txt, int *suffArr, int n)
{
    int m = strlen(pat);  // get length of pattern, needed for strncmp()
 
    // Do a simple binary search for the pattern in the text using the
    // suffix array
    int l = 0, r = n-1;  // Initialize left and right indexes
    while (l <= r)
    {
        // See if 'pat' is the prefix of the middle suffix in the suffix array
        int mid = l + (r - l)/2;
        int res = strncmp(pat, txt+suffArr[mid], m);
 
        // If a match is found at the middle, print it and return
        if (res == 0)
        {
            cout << "Pattern found at index " << suffArr[mid];
            return;
        }
 
        // Move to the left half if pattern is alphabtically less than
        // the mid suffix
        if (res < 0) r = mid - 1;
 
        // Otherwise move to the right half
        else l = mid + 1;
    }
 
    // We reach here if return statement in loop is not executed
    cout << "Pattern not found";
}
 
// Driver program to test above function
int main()
{
    char txt[] = "banana";  // text
    char pat[] = "nan";   // pattern to be searched in text
 
    // Build suffix array
    int n = strlen(txt);
    int *suffArr = buildSuffixArray(txt, n);
 
    // search pat in txt using the built suffix array
    search(pat, txt, suffArr, n);
 
    return 0;
}