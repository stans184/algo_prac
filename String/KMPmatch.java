public class KMPmatch {                                     //  브루트-포스법보다는 복잡하고, 보이어-무어법보다는 성능이 좋지 않아서 잘 사용하지 않음
    static int kmpMatch(String txt, String pat){            //  KMP matching, 이전에 진행했던 비교 data를 바탕으로 후속 data의 비교를 진행하는 것
        int pt = 1;
        int pp = 0;
        int[] skip = new int[pat.length()+1];

        skip[pt] = 0;                   //  건너뛰기 표를 만든다
        while(pt != pat.length()){
            if(pat.charAt(pt) == pat.charAt(pp))
                skip[++pt] = ++pp;
            else if(pp==0)
                skip[++pt] = pp;
            else
                pp = skip[pp];
        }

        pt = pp = 0;                    //  검색
        while(pt != txt.length() && pp != pat.length()){
            if(txt.charAt(pt) == pat.charAt(pp)){
                pt++;
                pp++;
            }else if(pp == 0)
                pt++;
            else
                pp = skip[pp];
        }

        if(pp == pat.length())
            return pt-pp;
        return -1;
    }
}
