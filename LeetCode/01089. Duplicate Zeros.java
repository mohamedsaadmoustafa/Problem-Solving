class Solution {
    public void duplicateZeros(int[] arr) {
        List<Integer> tempArr = new ArrayList<>();
        for (int index = 0; index < arr.length; index++) {
            tempArr.add(arr[index]);
            if (arr[index] == 0)
                tempArr.add(0);
        }
        for (int index = 0; index < arr.length; index++) {
            arr[index] = tempArr.get(index);
        }
    }
}
