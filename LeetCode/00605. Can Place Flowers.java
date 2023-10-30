class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int length = flowerbed.length;

        if (length == 0)
            return true;

        if (n == 0)
            if (length == 0)
                return false;
            else if (length == 1)
                return true;

        if (length == 1)
            if (flowerbed[0]==0)
                return true;
            else
	            return false;

        for (int index = 0; index < length; index++) {
            if (n > 0) {
                if (index == 0) {
                    if (flowerbed[index] == 0 && flowerbed[index + 1] == 0) {
                        flowerbed[index] = 1;
                        n--;
                    }
                } else if (index == length - 1) {
                    if (flowerbed[index] == 0 && flowerbed[index - 1] == 0) {
                        flowerbed[index] = 1;
                        n--;
                    }
                } else {
                    if (flowerbed[index] == 0 && flowerbed[index - 1] == 0 && flowerbed[index + 1] == 0) {
                        flowerbed[index] = 1;
                        n--;
                    }
                }
            }
        }

        return n == 0;
    }
}

// refactor previous solution
class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        if (flowerbed.length == 0 || n == 0)
            return true;

        if (flowerbed.length == 1)
            return flowerbed[0] == 0;

        for (int i = 0; i < flowerbed.length; i++) {
            if (n > 0 && flowerbed[i] == 0 && (i == 0 || flowerbed[i - 1] == 0) && (i == flowerbed.length - 1 || flowerbed[i + 1] == 0)) {
                flowerbed[i] = 1;
                n--;
            }
        }

        return n == 0;
    }
}
