class Solution {
    public int maxTurbulenceSize(int[] arr) {
        int dpDown = 1;
        int dpUp = 1;
        int dpMax = 1;
        for (int i = 1; i < arr.length; ++i) {
            if (arr[i] > arr[i - 1]) {
                dpUp = dpDown + 1;
                dpDown = 1;
                dpMax = Math.max(dpMax, dpUp);
            } else if (arr[i] < arr[i - 1]) {
                dpDown = dpUp + 1;
                dpUp = 1;
                dpMax = Math.max(dpMax, dpDown);
            } else {
                dpUp = dpDown = 1;
            }
        }
        return dpMax;
    }
}