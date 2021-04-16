public class BMmatch {
    static int bmMatch(String txt, String pat){
        int pt, pp; // pointer of text, pointer of pattern
        int txtLen = txt.length();
        int patLen = pat.length();
        int[] skip = new int[Character.MAX_VALUE+1];    //   건너뛰기 표

        for( pt=0;pt<=Character.MAX_VALUE;pt++)         //  건너뛰기 표 만들기
            skip[pt] = patLen;
        for(pt=0;pt<patLen-1;pt++)
            skip[pat.charAt(pt)] = patLen-pt-1;

        while(pt<txtLen){                               // 검색
            pp = patLen-1;

            while(txt.charAt(pt) == pat.charAt(pp)){
                if(pp == 0) return pt;                  // 검색 성공
                pp--;
                pt--;
            }

            pt += (skip[txt.charAt(pt)] > patLen - pp) ? skip[txt.charAt(pt)] : patLen - pp;
        }
        return -1;          //  검색 실패
    }
}
