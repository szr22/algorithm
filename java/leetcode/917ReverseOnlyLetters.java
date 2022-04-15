package leetcode;

class Solution {
    public String reverseOnlyLetters(String s) {
        char[] arr = s.toCharArray();
        int low = 0;
        int high = arr.length - 1;
        while(low<high){
            if(Character.isLetter(arr[low]) && Character.isLetter(arr[high])){
                swap(low, high, arr);
                low++;
                high--;
            } else if(Character.isLetter(arr[low]) && !Character.isLetter(arr[high])){
                high--;
            } else if(!Character.isLetter(arr[low]) && Character.isLetter(arr[high])){
                low++;
            } else {
                low++;
                high--;
            }
        }
        return new String(arr);
    }

    private void swap(int i, int j, char arr[]){
        char tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
}