package leetcode;

import java.util.HashMap;

class Solution {
    public int maxNumberOfBalloons(String text) {
        String tmp = "balloon";
        HashMap<Character,Integer> hashMap= new HashMap<>();
        for (int i=0; i<tmp.length(); i++) {
            hashMap.put(tmp.charAt(i), 0);
        }
        for(char i:text.toCharArray()) {
            if(hashMap.containsKey(i)){
                hashMap.put(i, hashMap.get(i)+1);
            }
        }
        return(
            Math.min(hashMap.get('b'),
            Math.min(hashMap.get('a'),
            Math.min(hashMap.get('l')/2,
            Math.min(hashMap.get('o')/2,hashMap.get('n'))))));
    }
}
