import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer nt = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(nt.nextToken()); // 챕터 갯수
        int t = Integer.parseInt(nt.nextToken()); // 공부할 수 있는 시간
        int k, s;

        int[] dp = new int[t+1]; // 시간이 0~t까지 얻을 수 있는 점수의 최대치를 넣어줄거임

        for (int i = 0; i < n; i++) {
            StringTokenizer ks = new StringTokenizer(br.readLine());
            k = Integer.parseInt(ks.nextToken()); // 이 챕터의 예상 공부 시간
            s = Integer.parseInt(ks.nextToken()); // 이 챕터의 문제 배점

            for (int j = t; j >= k; j--) {
                dp[j] = Math.max(dp[j], dp[j - k] + s);
            }
        }

        System.out.println(dp[t]);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}