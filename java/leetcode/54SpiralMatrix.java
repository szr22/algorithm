package leetcode;

class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> list=new ArrayList<>();
        int colStart=0,rowStart=0,colEnd=matrix[0].length-1,rowEnd=matrix.length-1;
        while(colStart<=colEnd && rowStart<=rowEnd){
            for(int i=colStart;i<=colEnd;i++)
                if(colStart<=colEnd && rowStart<=rowEnd)
                    list.add(matrix[rowStart][i]);
                rowStart++;
            for(int i=rowStart;i<=rowEnd;i++)
                if(colStart<=colEnd && rowStart<=rowEnd)
                    list.add(matrix[i][colEnd]);
                colEnd--;
            for(int i=colEnd;i>=colStart;i--)
                if(colStart<=colEnd && rowStart<=rowEnd)
                    list.add(matrix[rowEnd][i]);
                rowEnd--;
            for(int i=rowEnd;i>=rowStart;i--)
                if(colStart<=colEnd && rowStart<=rowEnd)
                    list.add(matrix[i][colStart]);
                colStart++;
        }
        return list;
    }
}