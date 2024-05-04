#include <iostream>
#include <vector>

int main()
{
    // Define the range of digits
    std::vector<int> digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

    // Define the uppercase letters
    std::vector<char> uppercase_letters = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

    for (int d1 : digits)
    {
        for (int d2 : digits)
        {
            for (int d3 : digits)
            {
                for (int d4 : digits)
                {
                    for (int d5 : digits)
                    {
                        for (int d6 : digits)
                        {
                            for (char l1 : uppercase_letters)
                            {
                                for (char l2 : uppercase_letters)
                                {
                                    std::cout << d1 << d2 << d3 << d4 << d5 << d6 << l1 << l2 << std::endl;
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    return 0;
}