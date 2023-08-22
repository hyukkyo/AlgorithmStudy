import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());

        int[][] ranges = new int[N][2];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            ranges[i][0] = Integer.parseInt(st.nextToken()); // 시작
            ranges[i][1] = Integer.parseInt(st.nextToken()); // 끝
        }

        Arrays.sort(ranges, (o1, o2) -> {
            if (o1[0] == o2[0])
                return o1[1] - o2[1];
            else
                return o1[0] - o2[0];
        });

        int count = 0;
        int range = 0;
        for (int i = 0; i < N; i++) {
            if (ranges[i][0] > range) {
                range = ranges[i][0]; // 시작
            }

            if (ranges[i][1] > range) { // 끝
                while (ranges[i][1] > range) {
                    range += L;
                    count++;
                }
            }
        }

        System.out.println(count);

    }
}