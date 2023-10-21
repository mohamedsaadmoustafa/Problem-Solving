class Solution {
    public static int findMaxStream(int[] arr){
        return Arrays.stream(arr).max().getAsInt();
    }
  
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> result = new ArrayList<>();
        int max = findMaxStream(candies);
        for (int candie : candies){
            if (candie+extraCandies >= max)
                result.add(true);
            else
                result.add(false);
        }
        return result;
    }
}
